# MCP Servers - Model Context Protocol

Esta configuración incluye 9 MCP servers habilitados más el poderoso **Zen MCP** con herramientas avanzadas de desarrollo.

## Tabla de Contenidos

- [¿Qué son los MCP Servers?](#qué-son-los-mcp-servers)
- [Servers Instalados](#servers-instalados)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Casos de Uso](#casos-de-uso)

## ¿Qué son los MCP Servers?

Model Context Protocol (MCP) es un estándar para extender las capacidades de Claude Code mediante servidores que proporcionan:

- **Tools**: Funciones que Claude puede ejecutar
- **Resources**: Datos y contexto adicional
- **Prompts**: Templates de prompts reutilizables

## Servers Instalados

### 1. 🧠 memory

**Propósito**: Almacenamiento persistente de conocimiento

**Funcionalidades**:
- Crear y gestionar entidades en un grafo de conocimiento
- Establecer relaciones entre entidades
- Agregar observaciones a entidades existentes
- Búsqueda en el grafo de conocimiento
- Lectura completa del grafo

**Tools disponibles**:
- `mcp__memory__create_entities` - Crear múltiples entidades
- `mcp__memory__create_relations` - Crear relaciones
- `mcp__memory__add_observations` - Agregar observaciones
- `mcp__memory__delete_entities` - Eliminar entidades
- `mcp__memory__delete_observations` - Eliminar observaciones
- `mcp__memory__delete_relations` - Eliminar relaciones
- `mcp__memory__read_graph` - Leer el grafo completo
- `mcp__memory__search_nodes` - Buscar nodos
- `mcp__memory__open_nodes` - Abrir nodos específicos

**Casos de uso**:
- Recordar preferencias del usuario a través de sesiones
- Mantener contexto de proyectos
- Almacenar decisiones arquitectónicas
- Construir base de conocimiento

**Instalación**:
```bash
# Ya incluido en Claude Code, solo necesita habilitarse
```

---

### 2. 🎭 executeautomation-playwright-server

**Propósito**: Automatización web y testing con Playwright

**Funcionalidades**:
- Navegar a URLs y capturar screenshots
- Interactuar con elementos (click, fill, select, hover)
- Ejecutar JavaScript en el navegador
- Capturar console logs del navegador
- Subir archivos
- Generar tests automáticamente

**Tools disponibles**:
- `playwright_navigate` - Navegar a URL
- `playwright_screenshot` - Capturar screenshot
- `playwright_click` - Click en elemento
- `playwright_fill` - Llenar campo de input
- `playwright_evaluate` - Ejecutar JavaScript
- `playwright_console_logs` - Obtener console logs
- `playwright_get_visible_html` - Obtener HTML visible
- Y muchas más...

**Casos de uso**:
- Automatización de tests E2E
- Web scraping
- Generación automática de tests
- Debugging de aplicaciones web

**Instalación**:
```bash
npm install -g @executeautomation/playwright-server
```

---

### 3. 🌐 fetch (DDG Search)

**Propósito**: Búsqueda web con DuckDuckGo

**Funcionalidades**:
- Búsqueda web sin tracking
- Obtener contenido de páginas web
- Resultados de búsqueda formateados

**Tools disponibles**:
- `mcp__ddg-search__search` - Búsqueda en DuckDuckGo
- `mcp__ddg-search__fetch_content` - Obtener contenido de URL

**Casos de uso**:
- Investigación de información actualizada
- Fact-checking
- Recopilar datos de múltiples fuentes

**Instalación**:
```bash
# Implementación mediante MCP ddg-search
# Configuración automática
```

---

### 4. 🐙 github

**Propósito**: Integración completa con GitHub

**Funcionalidades**:
- Gestión de repositorios (crear, fork, branch)
- Issues y pull requests
- Commits y push de archivos
- Búsqueda de código
- Reviews y merges

**Tools disponibles**:
- `mcp__github__create_repository` - Crear repo
- `mcp__github__create_or_update_file` - Crear/actualizar archivo
- `mcp__github__push_files` - Push múltiples archivos
- `mcp__github__create_pull_request` - Crear PR
- `mcp__github__create_issue` - Crear issue
- `mcp__github__search_repositories` - Buscar repos
- `mcp__github__search_code` - Buscar código
- Y muchas más...

**Casos de uso**:
- Automatización de workflows de GitHub
- Creación de PRs desde Claude
- Búsqueda en código de repos públicos
- Gestión de issues

**Instalación**:
```bash
# Requiere token de GitHub
# Configurar en variables de entorno: GITHUB_TOKEN
```

---

### 5. 🐘 postgresql

**Propósito**: Gestión de bases de datos PostgreSQL

**Funcionalidades**:
- Ejecutar queries SQL
- Gestión de esquemas
- Backup y restore
- Análisis de rendimiento

**Casos de uso**:
- Consultas a bases de datos
- Migraciones de esquema
- Análisis de datos

**Instalación**:
```bash
npm install -g @modelcontextprotocol/server-postgresql

# Configurar connection string:
# postgresql://user:password@localhost:5432/database
```

---

### 6. 🔧 code-executor

**Propósito**: Ejecutar código TypeScript/JavaScript en sandbox seguro

**Funcionalidades**:
- Ejecución de TypeScript/JavaScript en Deno sandbox
- Acceso controlado a herramientas MCP
- Descubrimiento de tools en runtime
- Límites de tiempo y recursos
- Permisos de sandbox configurables

**Tools disponibles**:
- `mcp__code-executor__executeTypescript` - Ejecutar código TS/JS
- `mcp__code-executor__health` - Estado del servidor

**Funciones disponibles en el sandbox**:
- `callMCPTool(toolName, params)` - Llamar otros MCP tools
- `discoverMCPTools(options)` - Descubrir tools disponibles
- `getToolSchema(toolName)` - Obtener schema de tool
- `searchTools(query, limit)` - Buscar tools por keywords

**Casos de uso**:
- Prototipado rápido de código
- Automatización compleja con múltiples MCPs
- Workflows personalizados
- Testing de lógica

**Instalación**:
```bash
# Requiere Deno
deno --version

# Si no está instalado:
# Windows
powershell -Command "irm https://deno.land/install.ps1 | iex"

# Linux/macOS
curl -fsSL https://deno.land/install.sh | sh
```

---

### 7. 📚 context7

**Propósito**: Documentación actualizada de librerías y frameworks

**Funcionalidades**:
- Resolver IDs de librerías
- Obtener documentación actualizada
- Modo code (APIs y ejemplos) y modo info (guías conceptuales)
- Paginación para grandes documentaciones

**Tools disponibles**:
- `mcp__context7__resolve-library-id` - Resolver nombre a ID de librería
- `mcp__context7__get-library-docs` - Obtener documentación

**Casos de uso**:
- Consultar documentación oficial sin salir de Claude
- Obtener ejemplos actualizados de código
- Verificar APIs de versiones específicas

**Instalación**:
```bash
# Instalación automática desde marketplace
# No requiere configuración adicional
```

**Ejemplo de uso**:
```typescript
// 1. Resolver librería
resolve-library-id("react")
// Retorna: /facebook/react

// 2. Obtener docs
get-library-docs("/facebook/react", mode: "code", topic: "hooks")
```

---

### 8. 🔍 ddg-search

**Propósito**: Búsqueda web con DuckDuckGo (implementación alternativa)

Ver descripción en [fetch](#3--fetch-ddg-search)

---

### 9. 📊 excel

**Propósito**: Manipulación avanzada de archivos Excel

**Funcionalidades**:
- Leer y escribir datos
- Aplicar fórmulas
- Formato de celdas
- Crear tablas y gráficos
- Crear pivot tables
- Validación de datos
- Merge/unmerge celdas

**Tools disponibles**:
- `mcp__excel__read_data_from_excel` - Leer datos
- `mcp__excel__write_data_to_excel` - Escribir datos
- `mcp__excel__apply_formula` - Aplicar fórmula
- `mcp__excel__validate_formula_syntax` - Validar fórmula
- `mcp__excel__format_range` - Formatear rango
- `mcp__excel__create_chart` - Crear gráfico
- `mcp__excel__create_pivot_table` - Crear pivot table
- `mcp__excel__create_table` - Crear tabla Excel
- `mcp__excel__merge_cells` - Combinar celdas
- Y muchas más...

**Casos de uso**:
- Automatización de reportes
- Análisis de datos en Excel
- Generación de gráficos dinámicos
- Manipulación de archivos Excel complejos

**Instalación**:
```bash
pip install openpyxl pandas
```

---

## 🎯 Zen MCP - Suite Avanzada

Además de los MCPs estándar, esta configuración incluye el poderoso **Zen MCP** con herramientas avanzadas.

### Tools de Zen MCP

#### 1. `chat` - Colaboración con múltiples modelos
Conversar con diferentes modelos de IA para obtener perspectivas diversas.

**Parámetros**:
- `prompt` - La pregunta o idea
- `model` - Modelo a usar (gemini-2.5-pro, gemini-3-pro-preview, etc.)
- `continuation_id` - ID para conversaciones multi-turno
- `temperature` - 0 (determinístico) a 1 (creativo)
- `thinking_mode` - minimal, low, medium, high, max

#### 2. `thinkdeep` - Investigación y razonamiento profundo
Análisis multi-etapa para problemas complejos, decisiones arquitectónicas y análisis de seguridad.

**Parámetros**:
- `step` - Contenido del paso actual
- `hypothesis` - Teoría sobre el issue
- `findings` - Descubrimientos importantes
- `confidence` - exploring, low, medium, high, very_high, almost_certain, certain
- `next_step_required` - Si se necesita otro paso

#### 3. `planner` - Planificación interactiva
Planificación secuencial con capacidad de revisión y branching.

**Parámetros**:
- `step` - Contenido de planificación
- `step_number` - Número de paso actual
- `total_steps` - Pasos totales estimados
- `is_branch_point` - Si crea una nueva branch
- `is_step_revision` - Si reemplaza un paso previo

#### 4. `consensus` - Consenso multi-modelo
Construye consenso consultando múltiples modelos con diferentes posiciones.

**Parámetros**:
- `step` - Propuesta/pregunta o notas internas
- `models` - Lista de modelos a consultar (mínimo 2)
- `findings` - Tu análisis o resumen de respuestas
- `current_model_index` - Índice del siguiente modelo

#### 5. `codereview` - Revisión sistemática de código
Revisión paso a paso con validación experta.

**Parámetros**:
- `step` - Narrativa de revisión
- `findings` - Findings positivos y negativos
- `issues_found` - Issues con severidad
- `review_type` - full, security, performance, quick
- `review_validation_type` - external o internal

#### 6. `precommit` - Validación pre-commit
Valida cambios git y estado del repositorio antes de commit.

**Parámetros**:
- `path` - Path al repositorio
- `step` - Cómo validarás los cambios
- `findings` - Insights de git diff, riesgos, etc.
- `include_staged` - Inspeccionar staged changes
- `include_unstaged` - Inspeccionar unstaged changes

#### 7. `debug` - Debugging sistemático
Debugging y análisis de causa raíz para cualquier tipo de issue.

**Parámetros**:
- `step` - Paso de investigación
- `hypothesis` - Teoría sobre la causa raíz
- `findings` - Descubrimientos y evidencia
- `confidence` - Nivel de confianza en la hipótesis

#### 8. `challenge` - Pensamiento crítico
Previene acuerdo reflexivo forzando pensamiento crítico cuando una afirmación es desafiada.

**Parámetros**:
- `prompt` - Afirmación a escrutinizar

#### 9. `apilookup` - Documentación de APIs actualizada
Busca documentación oficial, info de versiones, breaking changes y guías de migración.

**Parámetros**:
- `prompt` - API, SDK, librería o tecnología para buscar docs

#### 10. `listmodels` - Listar modelos disponibles
Muestra proveedores de modelos de IA configurados y modelos disponibles.

---

## Instalación

### Configuración en settings.local.json

Los MCPs se habilitan en `settings.local.json`:

```json
{
  "enableAllProjectMcpServers": true,
  "enabledMcpjsonServers": [
    "memory",
    "executeautomation-playwright-server",
    "fetch",
    "github",
    "postgresql",
    "code-executor",
    "context7",
    "ddg-search",
    "excel"
  ]
}
```

### Instalación Individual

Cada MCP server tiene sus propios requisitos:

1. **memory**: Built-in, no requiere instalación
2. **playwright**: `npm install -g @executeautomation/playwright-server`
3. **github**: Requiere `GITHUB_TOKEN` en env vars
4. **postgresql**: Requiere PostgreSQL y connection string
5. **code-executor**: Requiere Deno
6. **context7**: Built-in desde marketplace
7. **excel**: Requiere `pip install openpyxl pandas`
8. **ddg-search**: Built-in desde marketplace

Ver [INSTALLATION.md](../INSTALLATION.md) para instrucciones completas.

## Configuración

### Variables de Entorno

Algunos MCPs requieren variables de entorno:

```json
{
  "env": {
    "GITHUB_TOKEN": "tu_token_aqui",
    "POSTGRES_CONNECTION": "postgresql://user:pass@localhost:5432/db"
  }
}
```

### Permisos

Los MCPs requieren permisos específicos en `settings.local.json`:

```json
{
  "permissions": {
    "allow": [
      "mcp__github__search_repositories",
      "mcp__code-executor__executeTypescript",
      "mcp__code-executor__health"
    ]
  }
}
```

## Casos de Uso

### Workflow Completo: Feature Development

```
1. Usar `github` para crear branch
2. Desarrollar feature con Claude
3. Usar `codereview` (Zen) para revisar
4. Usar `precommit` (Zen) para validar cambios
5. Usar `github` para crear PR
6. Usar `playwright` para tests E2E
```

### Research & Documentation

```
1. Usar `ddg-search` para investigación inicial
2. Usar `context7` para docs oficiales
3. Usar `consensus` (Zen) para validar enfoques
4. Usar `memory` para almacenar decisiones
```

### Data Analysis

```
1. Usar `postgresql` para queries
2. Usar `excel` para análisis y visualización
3. Usar `code-executor` para procesamiento custom
4. Generar reportes automatizados
```

### Debugging Complex Issues

```
1. Usar `debug` (Zen) para análisis sistemático
2. Usar `thinkdeep` (Zen) para investigación profunda
3. Usar `playwright` para reproducir bugs
4. Usar `github` para buscar issues similares
```

---

## Troubleshooting

### MCP no aparece en tools

1. Verifica que esté en `enabledMcpjsonServers`
2. Asegúrate de que esté instalado correctamente
3. Reinicia Claude Code
4. Revisa los logs de Claude Code

### Error de permisos

1. Agrega el tool a `permissions.allow` en `settings.local.json`
2. O configura `"defaultMode": "ask"` para que pregunte

### Error de conexión

1. Verifica que el servicio esté corriendo (PostgreSQL, etc.)
2. Revisa las credenciales en variables de entorno
3. Confirma connectivity (firewall, network)

---

Para más información, ver:
- [INSTALLATION.md](../INSTALLATION.md) - Guía de instalación
- [ENVIRONMENT_VARIABLES.md](ENVIRONMENT_VARIABLES.md) - Variables de entorno
- [PERMISSIONS.md](PERMISSIONS.md) - Sistema de permisos
