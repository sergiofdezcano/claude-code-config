# Claude Code Configuration Backup

Backup completo de mi configuración personalizada de Claude Code con agentes especializados, MCP servers, scripts y documentación detallada.

**Fecha del backup:** Diciembre 2025
**Claude Code Version:** Latest

## Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Características Principales](#características-principales)
- [Instalación Rápida](#instalación-rápida)
- [Documentación Detallada](#documentación-detallada)
- [Requisitos](#requisitos)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

## Descripción General

Este repositorio contiene una configuración avanzada de Claude Code optimizada para desarrollo profesional. Incluye:

- **9 Agentes Especializados**: Desde revisión de código hasta optimización de bases de datos
- **9 MCP Servers**: Integraciones con GitHub, PostgreSQL, Excel, Playwright y más
- **Script de Monitoreo**: Visualización en tiempo real del uso de contexto y costos
- **Configuración de Permisos**: Sistema de permisos preconfigurado para operaciones seguras
- **Comando Personalizado**: Generador de documentación

## Estructura del Repositorio

```
claude-code-config/
├── README.md                          # Este archivo
├── INSTALLATION.md                    # Guía de instalación paso a paso
├── config/
│   ├── settings.json                  # Configuración base de permisos
│   └── settings.local.json            # Configuración local con MCPs y env vars
├── agents/
│   ├── README.md                      # Documentación detallada de cada agente
│   ├── api-documenter.md              # Documentación de APIs (OpenAPI/Swagger)
│   ├── code-reviewer.md               # Revisión de código y seguridad
│   ├── data-engineer.md               # Pipelines ETL/ELT y Spark
│   ├── database-architect.md          # Diseño de arquitecturas de datos
│   ├── database-optimizer.md          # Optimización de queries y rendimiento
│   ├── prompt-engineer.md             # Optimización de prompts para LLMs
│   ├── python-pro.md                  # Código Python avanzado
│   ├── search-specialist.md           # Investigación y síntesis web
│   └── technical-writer.md            # Documentación técnica
├── commands/
│   ├── README.md                      # Documentación de comandos
│   └── documentation-generator.md     # /documentation-generator command
├── scripts/
│   ├── README.md                      # Documentación de scripts
│   └── context-monitor.py             # Monitoreo de contexto en status line
├── docs/
│   ├── MCP_SERVERS.md                 # Documentación de MCP servers
│   ├── ENVIRONMENT_VARIABLES.md       # Variables de entorno
│   └── PERMISSIONS.md                 # Sistema de permisos
└── .gitignore
```

## Características Principales

### 🤖 Agentes Especializados

Los agentes se invocan automáticamente cuando detectan tareas relevantes:

- **code-reviewer**: Revisión proactiva después de escribir código
- **api-documenter**: Generación de specs OpenAPI y SDKs
- **python-pro**: Refactorización y optimización Python
- **database-architect**: Diseño de arquitecturas de datos complejas
- **database-optimizer**: Optimización de queries y índices
- **data-engineer**: Pipelines ETL/ELT con Airflow y Spark
- **prompt-engineer**: Optimización de prompts para LLMs
- **search-specialist**: Investigación profunda con síntesis
- **technical-writer**: Guías de usuario y documentación

Ver [agents/README.md](agents/README.md) para documentación completa.

### 🔌 MCP Servers

9 MCP servers habilitados para funcionalidad extendida:

| MCP Server | Propósito | Destacado |
|-----------|----------|-----------|
| **memory** | Almacenamiento persistente de conocimiento | ⭐ |
| **github** | Integración completa con GitHub | ⭐ |
| **code-executor** | Ejecutar TypeScript/JavaScript en sandbox | ⭐ |
| **context7** | Documentación actualizada de librerías | ⭐ |
| **playwright** | Automatización web y testing | |
| **postgresql** | Gestión de bases de datos PostgreSQL | |
| **excel** | Manipulación avanzada de archivos Excel | |
| **ddg-search** | Búsqueda web con DuckDuckGo | |
| **fetch** | Consultas web optimizadas | |

Además incluye **Zen MCP** con herramientas avanzadas: `chat`, `thinkdeep`, `planner`, `consensus`, `codereview`, `precommit`, `debug`, `challenge`, `apilookup`.

Ver [docs/MCP_SERVERS.md](docs/MCP_SERVERS.md) para más detalles.

### 📊 Script de Monitoreo de Contexto

El script `context-monitor.py` muestra en la barra de estado:

- 🧠 **Uso de contexto** con barra de progreso visual
- 💰 **Costo de la sesión** en tiempo real
- ⏱ **Duración de la sesión**
- 📝 **Líneas de código cambiadas** (+/-)
- 🎨 **Alertas visuales** cuando el contexto está alto

![Context Monitor Preview](https://via.placeholder.com/600x60/2e2e2e/00ff00?text=Status+Line+Preview)

### ⚙️ Variables de Entorno Configuradas

```json
{
  "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "8000",
  "DISABLE_NON_ESSENTIAL_MODEL_CALLS": "1",
  "DISABLE_COST_WARNINGS": "1"
}
```

Ver [docs/ENVIRONMENT_VARIABLES.md](docs/ENVIRONMENT_VARIABLES.md) para detalles.

## Instalación Rápida

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/claude-code-config.git
cd claude-code-config

# 2. Copiar archivos de configuración
# Windows
copy config\settings.json %USERPROFILE%\.claude\settings.json
copy config\settings.local.json %USERPROFILE%\.claude\settings.local.json

# Linux/macOS
cp config/settings.json ~/.claude/settings.json
cp config/settings.local.json ~/.claude/settings.local.json

# 3. Copiar agentes
# Windows
xcopy agents %USERPROFILE%\.claude\agents\ /E /I

# Linux/macOS
cp -r agents ~/.claude/agents/

# 4. Copiar comandos y scripts
# Windows
xcopy commands %USERPROFILE%\.claude\commands\ /E /I
xcopy scripts %USERPROFILE%\.claude\scripts\ /E /I

# Linux/macOS
cp -r commands ~/.claude/commands/
cp -r scripts ~/.claude/scripts/

# 5. Instalar MCPs (ver INSTALLATION.md para instrucciones detalladas)
```

Para instrucciones completas incluyendo instalación de MCPs, ver [INSTALLATION.md](INSTALLATION.md).

## Documentación Detallada

- **[INSTALLATION.md](INSTALLATION.md)** - Guía de instalación completa paso a paso
- **[agents/README.md](agents/README.md)** - Documentación de todos los agentes
- **[docs/MCP_SERVERS.md](docs/MCP_SERVERS.md)** - Guía de MCP servers
- **[docs/ENVIRONMENT_VARIABLES.md](docs/ENVIRONMENT_VARIABLES.md)** - Variables de entorno
- **[docs/PERMISSIONS.md](docs/PERMISSIONS.md)** - Sistema de permisos

## Requisitos

- **Claude Code** (versión más reciente)
- **Python 3.8+** (para el script de monitoreo)
- **Git** (para clonar el repositorio)
- **Node.js 16+** (para algunos MCP servers)

### Requisitos Opcionales por MCP

- **PostgreSQL** - Para el MCP de postgresql
- **Deno** - Para code-executor MCP
- **Playwright** - Para automatización web

Ver requisitos completos en [INSTALLATION.md](INSTALLATION.md).

## Casos de Uso

### Revisión de Código Automática
```bash
# El agente code-reviewer se activa automáticamente después de escribir código
# Revisa seguridad, rendimiento, calidad y mejores prácticas
```

### Documentación de APIs
```bash
# El agente api-documenter genera specs OpenAPI completas
# Incluye ejemplos, autenticación, códigos de error y SDKs
```

### Optimización de Bases de Datos
```bash
# El agente database-optimizer analiza queries lentas
# Sugiere índices, reescribe queries y optimiza el esquema
```

### Monitoreo de Contexto
```bash
# El script context-monitor muestra uso de contexto en tiempo real
# Ayuda a prevenir truncamiento de conversaciones
```

## Personalización

Todos los archivos son completamente personalizables:

1. **Agentes**: Edita los archivos `.md` en `agents/` para ajustar comportamientos
2. **Permisos**: Modifica `settings.json` y `settings.local.json`
3. **MCPs**: Habilita/deshabilita en `settings.local.json` → `enabledMcpjsonServers`
4. **Status Line**: Personaliza `scripts/context-monitor.py`

## Troubleshooting

### Los agentes no se activan

Verifica que los archivos estén en `~/.claude/agents/` y tengan el formato correcto de frontmatter YAML.

### El script de monitoreo no funciona

Asegúrate de tener Python 3.8+ instalado y que la ruta del script sea correcta en `settings.local.json`.

### Los MCPs no aparecen

Verifica que estén instalados y habilitados en `enabledMcpjsonServers` en `settings.local.json`.

Ver más soluciones en [INSTALLATION.md](INSTALLATION.md#troubleshooting).

## Contribuir

Las contribuciones son bienvenidas:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## Licencia

MIT License - Ver [LICENSE](LICENSE) para detalles.

## Agradecimientos

- [Anthropic](https://anthropic.com) por Claude Code
- Comunidad de MCP servers
- Todos los contribuidores

---

**Nota**: Este es un backup personal. Adapta los paths y configuraciones según tu sistema operativo y necesidades.

Para soporte o preguntas, abre un issue en GitHub.
