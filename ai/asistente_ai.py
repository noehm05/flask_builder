
import os
import logging
from flask import Blueprint, request, jsonify
from openai import OpenAI

logger = logging.getLogger(__name__)

asistente_bp = Blueprint(
    "asistente_ai",
    __name__,
    url_prefix="/api"
)


def obtener_cliente():
    """Crea el cliente de conexión con la API de IA."""
    api_key = os.getenv("AI_API_KEY")
    base_url = os.getenv("AI_URL")

    if not api_key:
        raise RuntimeError("No se configuró AI_API_KEY.")

    if not base_url:
        raise RuntimeError("No se configuró AI_URL.")

    return OpenAI(
        api_key=api_key,
        base_url=base_url
    )


@asistente_bp.post("/asistente")
def consultar_asistente():
    try:
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({
                "error": "Se esperaba una solicitud JSON válida."
            }), 400

        mensaje = data.get("message", "").strip()
        historial = data.get("history", [])

        if not mensaje:
            return jsonify({
                "error": "Debes escribir un mensaje."
            }), 400

        if not isinstance(historial, list):
            return jsonify({
                "error": "El historial debe ser una lista."
            }), 400

        mensajes = [
            {
                "role": "system",
                "content": (
                    "Eres un asistente de inteligencia artificial "
                    "especializado en cocina, repostería, recetas, "
                    "ingredientes, técnicas culinarias y sustituciones "
                    "de ingredientes. Responde en español, de forma "
                    "clara, práctica y ordenada. Cuando sea pertinente, "
                    "indica cantidades, porciones, tiempos y pasos."
                )
            }
        ]

        for item in historial[-20:]:
            if not isinstance(item, dict):
                continue

            rol = item.get("role")
            contenido = item.get("content")

            if (
                rol in ("user", "assistant")
                and isinstance(contenido, str)
                and contenido.strip()
            ):
                mensajes.append({
                    "role": rol,
                    "content": contenido.strip()
                })

        mensajes.append({
            "role": "user",
            "content": mensaje
        })

        cliente = obtener_cliente()

        respuesta = cliente.chat.completions.create(
            model=os.getenv("AI_MODEL", "gpt-4o-mini"),
            messages=mensajes,
            temperature=0.7
        )

        contenido = respuesta.choices[0].message.content

        if not contenido:
            contenido = "No se recibió una respuesta de la IA."

        return jsonify({
            "respuesta": contenido
        }), 200

    except Exception:
        logger.exception("Error al consultar el asistente de IA.")

        return jsonify({
            "error": (
                "No se pudo obtener una respuesta. "
                "Verifica la configuración de la API e inténtalo nuevamente."
            )
        }), 500