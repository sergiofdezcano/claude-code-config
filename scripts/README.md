# Scripts

Scripts personalizados para extender la funcionalidad de Claude Code.

## Scripts Disponibles

### context-monitor.py

Script de monitoreo de contexto en tiempo real para la barra de estado de Claude Code.

**Características**:
- 🧠 Visualización de uso de contexto con barra de progreso
- 💰 Tracking de costos de la sesión en tiempo real
- ⏱ Duración de la sesión
- 📝 Líneas de código cambiadas (+/-)
- 🎨 Alertas visuales codificadas por color
- 📊 Métricas de rendimiento

**Output de ejemplo**:
```
[Claude Sonnet] 📁 mi-proyecto 🧠 🟢████████ 45% 💰 $0.023 ⏱ 15m 📝 +127
```

**Indicadores de Color**:
- 🟢 Verde: 0-50% de contexto usado (seguro)
- 🟡 Amarillo: 50-75% (precaución)
- 🟠 Naranja: 75-90% (alto)
- 🔴 Rojo: 90-95% (crítico)
- 🚨 Rojo parpadeante: >95% (urgente)

### Cómo Funciona

1. Claude Code ejecuta el script y le pasa JSON con información de la sesión
2. El script parsea el JSON y extrae métricas
3. Genera una línea formateada con colores ANSI
4. Claude Code muestra el output en la barra de estado

### Requisitos

- Python 3.8 o superior
- Módulos estándar: json, sys, os, re

### Instalación

```bash
# Copiar script
# Windows
copy scripts\context-monitor.py %USERPROFILE%\.claude\scripts\context-monitor.py

# Linux/macOS
cp scripts/context-monitor.py ~/.claude/scripts/context-monitor.py
chmod +x ~/.claude/scripts/context-monitor.py
```

### Configuración

En `settings.local.json`:

```json
{
  "statusLine": {
    "type": "command",
    "command": "python .claude/scripts/context-monitor.py"
  }
}
```

**Nota para Linux/macOS**: Usa `python3` si `python` apunta a Python 2:

```json
{
  "statusLine": {
    "type": "command",
    "command": "python3 .claude/scripts/context-monitor.py"
  }
}
```

### Personalización

Puedes modificar el script para:

#### Cambiar Umbrales de Color

```python
# Línea ~89-103
if percent >= 95:
    icon, color = "🚨", "\033[31;1m"  # Cambiar umbral a 98
elif percent >= 90:
    icon, color = "🔴", "\033[31m"     # Cambiar umbral a 92
# ...
```

#### Cambiar Formato de Display

```python
# Línea ~105-119
segments = 10  # Más segmentos = barra más larga
bar = "█" * filled + "▁" * (segments - filled)
```

#### Agregar Nuevas Métricas

```python
def get_custom_metric(data):
    """Agregar tu propia métrica."""
    # Tu código aquí
    return formatted_metric

# En main():
custom = get_custom_metric(data)
status_line = f"{model_display} {custom} ..."
```

### Debugging

```bash
# Probar el script manualmente
echo '{"model":{"display_name":"Claude"},"workspace":{"current_dir":"/test"}}' | python ~/.claude/scripts/context-monitor.py

# Ver output esperado
[Claude] 📁 test 🧠 🔵 ???
```

### Troubleshooting

#### Error: "python: command not found"

**Linux/macOS**:
```bash
# Instalar Python
# Ubuntu/Debian
sudo apt install python3

# macOS
brew install python3

# Actualizar settings.local.json
"command": "python3 .claude/scripts/context-monitor.py"
```

#### El script no se ejecuta

1. Verificar permisos (Linux/macOS):
```bash
chmod +x ~/.claude/scripts/context-monitor.py
```

2. Verificar sintaxis del script:
```bash
python ~/.claude/scripts/context-monitor.py --help
```

3. Verificar configuración en settings.local.json:
```bash
cat ~/.claude/settings.local.json | grep statusLine
```

#### Output incorrecto o con errores

1. Capturar output de debug:
```python
# Agregar al script (línea ~194)
import sys
print(f"DEBUG: {data}", file=sys.stderr)
```

2. Ver logs de Claude Code

3. Verificar formato de JSON de entrada

## Crear Nuevos Scripts

### Script de Example

```python
#!/usr/bin/env python3
"""
Mi Script Personalizado
"""
import json
import sys

def main():
    try:
        # Leer input de Claude Code
        data = json.load(sys.stdin)

        # Procesar data
        output = process_data(data)

        # Imprimir resultado
        print(output)

    except Exception as e:
        # Fallback en caso de error
        print(f"Error: {str(e)}")

def process_data(data):
    # Tu lógica aquí
    return "Mi output personalizado"

if __name__ == "__main__":
    main()
```

### Configurar el Script

```json
{
  "statusLine": {
    "type": "command",
    "command": "python .claude/scripts/mi-script.py"
  }
}
```

## Mejores Prácticas

1. **Manejo de Errores**: Siempre incluye try/except
2. **Fallback Display**: Proporciona output por defecto en caso de error
3. **Performance**: Los scripts deben ser rápidos (<100ms idealmente)
4. **Testing**: Prueba con diferentes inputs
5. **Documentación**: Comenta el código claramente

## Scripts Potenciales

Ideas para nuevos scripts:

### Git Status Monitor
```python
# Mostrar estado de git en status line
# Ejemplo: main↑2↓1 M:3 ?:1
```

### Docker Status
```python
# Mostrar containers corriendo
# Ejemplo: 🐳 3↑ 1↓
```

### System Resources
```python
# Mostrar CPU y memoria
# Ejemplo: CPU:45% MEM:8GB
```

### Task Tracker
```python
# Mostrar tareas pendientes
# Ejemplo: ✓ 5/10 tasks
```

---

Ver [../README.md](../README.md) para más información sobre la configuración completa.
