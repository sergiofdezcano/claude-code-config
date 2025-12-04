#!/usr/bin/env python3
"""Alerta cuando el uso de tokens es alto"""
import json
import sys

try:
    data = json.load(sys.stdin)

    # Intentar obtener usage de diferentes lugares posibles
    usage = data.get('token_usage', {})
    if not usage:
        usage = data.get('usage', {})

    used = usage.get('total_used', 0) or usage.get('input_tokens', 0)
    limit = usage.get('limit', 200000)

    if used > 0:
        percent = (used / limit) * 100

        if percent > 50:
            print(f"⚠️  WARNING: {percent:.0f}% contexto usado - SÉ BREVE", file=sys.stderr)
        elif percent > 30:
            print(f"⚡ {percent:.0f}% contexto - Modo eficiente", file=sys.stderr)
        else:
            print(f"✓ {percent:.0f}% contexto", file=sys.stderr)
    else:
        print("✓ Contexto OK", file=sys.stderr)

except Exception as e:
    # Silencioso en caso de error
    pass
