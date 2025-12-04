# Guía de Instalación

Guía completa paso a paso para instalar y configurar esta configuración de Claude Code.

## Tabla de Contenidos

- [Requisitos Previos](#requisitos-previos)
- [Instalación Rápida](#instalación-rápida)
- [Instalación Detallada](#instalación-detallada)
- [Instalación de MCP Servers](#instalación-de-mcp-servers)
- [Verificación](#verificación)
- [Troubleshooting](#troubleshooting)

## Requisitos Previos

### Requisitos Básicos

- **Claude Code** instalado y funcionando
- **Git** para clonar el repositorio
- **Python 3.8+** para el script de monitoreo

### Requisitos por Sistema Operativo

#### Windows
```powershell
# Verificar Python
python --version

# Verificar Git
git --version
```

#### Linux/macOS
```bash
# Verificar Python
python3 --version

# Verificar Git
git --version
```

### Requisitos Opcionales (por MCP)

| MCP Server | Requisito | Comando de Verificación |
|-----------|-----------|------------------------|
| code-executor | Deno | `deno --version` |
| postgresql | PostgreSQL Client | `psql --version` |
| playwright | Node.js 16+ | `node --version` |
| excel | Python + openpyxl | `pip list \| grep openpyxl` |
| github | GitHub Token | Variable de entorno |

## Instalación Rápida

### Windows

```powershell
# 1. Clonar repositorio
git clone https://github.com/TU_USUARIO/claude-code-config.git
cd claude-code-config

# 2. Copiar configuración
Copy-Item config\settings.json $env:USERPROFILE\.claude\settings.json
Copy-Item config\settings.local.json $env:USERPROFILE\.claude\settings.local.json

# 3. Copiar agentes
xcopy agents $env:USERPROFILE\.claude\agents\ /E /I

# 4. Copiar comandos
xcopy commands $env:USERPROFILE\.claude\commands\ /E /I

# 5. Copiar scripts
xcopy scripts $env:USERPROFILE\.claude\scripts\ /E /I

# 6. Reiniciar Claude Code
```

### Linux/macOS

```bash
# 1. Clonar repositorio
git clone https://github.com/TU_USUARIO/claude-code-config.git
cd claude-code-config

# 2. Copiar configuración
cp config/settings.json ~/.claude/settings.json
cp config/settings.local.json ~/.claude/settings.local.json

# 3. Copiar agentes
cp -r agents/* ~/.claude/agents/

# 4. Copiar comandos
cp -r commands/* ~/.claude/commands/

# 5. Copiar scripts
cp -r scripts/* ~/.claude/scripts/

# 6. Hacer ejecutable el script Python
chmod +x ~/.claude/scripts/context-monitor.py

# 7. Reiniciar Claude Code
```

## Instalación Detallada

### Paso 1: Backup de Configuración Existente

**IMPORTANTE**: Antes de instalar, haz backup de tu configuración actual.

```bash
# Windows
xcopy %USERPROFILE%\.claude %USERPROFILE%\.claude.backup\ /E /I

# Linux/macOS
cp -r ~/.claude ~/.claude.backup
```

### Paso 2: Clonar el Repositorio

```bash
git clone https://github.com/TU_USUARIO/claude-code-config.git
cd claude-code-config
```

### Paso 3: Revisar y Personalizar Configuración

Antes de copiar, revisa los archivos de configuración:

```bash
# Ver settings.json
cat config/settings.json

# Ver settings.local.json
cat config/settings.local.json
```

**Personaliza según necesites**:
- Rutas específicas de tu sistema
- MCPs que quieras habilitar/deshabilitar
- Permisos personalizados

### Paso 4: Copiar Archivos de Configuración

#### settings.json

```bash
# Windows
copy config\settings.json %USERPROFILE%\.claude\settings.json

# Linux/macOS
cp config/settings.json ~/.claude/settings.json
```

Este archivo contiene:
- Permisos básicos de git y bash
- Configuración de allow/deny/ask

#### settings.local.json

```bash
# Windows
copy config\settings.local.json %USERPROFILE%\.claude\settings.local.json

# Linux/macOS
cp config/settings.local.json ~/.claude/settings.local.json
```

Este archivo contiene:
- Variables de entorno
- Lista de MCPs habilitados
- Permisos adicionales
- Configuración de status line

**IMPORTANTE**: Adapta las rutas en `settings.local.json` a tu sistema:

```json
{
  "permissions": {
    "allow": [
      "Bash(dir C:Userssergi...)"  // Cambia "sergi" por tu usuario
    ]
  },
  "statusLine": {
    "command": "python .claude/scripts/context-monitor.py"  // Ajusta según tu OS
  }
}
```

### Paso 5: Copiar Agentes

```bash
# Windows
xcopy agents %USERPROFILE%\.claude\agents\ /E /I

# Linux/macOS
mkdir -p ~/.claude/agents
cp -r agents/* ~/.claude/agents/
```

**Verificar**:
```bash
# Windows
dir %USERPROFILE%\.claude\agents

# Linux/macOS
ls -la ~/.claude/agents/
```

Deberías ver 9 archivos `.md`.

### Paso 6: Copiar Comandos

```bash
# Windows
xcopy commands %USERPROFILE%\.claude\commands\ /E /I

# Linux/macOS
mkdir -p ~/.claude/commands
cp -r commands/* ~/.claude/commands/
```

### Paso 7: Copiar Scripts

```bash
# Windows
xcopy scripts %USERPROFILE%\.claude\scripts\ /E /I

# Linux/macOS
mkdir -p ~/.claude/scripts
cp -r scripts/* ~/.claude/scripts/
chmod +x ~/.claude/scripts/context-monitor.py
```

**Verificar Python**:
```bash
python --version  # Debe ser 3.8+
python scripts/context-monitor.py --help  # Prueba el script
```

### Paso 8: Reiniciar Claude Code

Reinicia Claude Code completamente para que cargue la nueva configuración.

## Instalación de MCP Servers

### 1. memory (Built-in)

Ya incluido en Claude Code. Solo necesita estar habilitado en `settings.local.json`.

### 2. github

```bash
# 1. Crear GitHub Personal Access Token
# Ve a: https://github.com/settings/tokens
# Scopes necesarios: repo, workflow, write:packages

# 2. Configurar token
# Windows
setx GITHUB_TOKEN "tu_token_aqui"

# Linux/macOS
echo 'export GITHUB_TOKEN="tu_token_aqui"' >> ~/.bashrc
source ~/.bashrc
```

### 3. code-executor

```bash
# Instalar Deno

# Windows
powershell -Command "irm https://deno.land/install.ps1 | iex"

# Linux/macOS
curl -fsSL https://deno.land/install.sh | sh

# Agregar al PATH
# Linux/macOS
echo 'export DENO_INSTALL="$HOME/.deno"' >> ~/.bashrc
echo 'export PATH="$DENO_INSTALL/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# Verificar
deno --version
```

### 4. playwright

```bash
# Instalar globalmente
npm install -g @executeautomation/playwright-server

# Instalar browsers
npx playwright install

# Verificar
playwright --version
```

### 5. postgresql

```bash
# Instalar MCP server
npm install -g @modelcontextprotocol/server-postgresql

# Configurar connection string
# Windows
setx POSTGRES_CONNECTION "postgresql://user:password@localhost:5432/database"

# Linux/macOS
echo 'export POSTGRES_CONNECTION="postgresql://user:password@localhost:5432/database"' >> ~/.bashrc
source ~/.bashrc
```

### 6. excel

```bash
# Instalar dependencias Python
pip install openpyxl pandas xlsxwriter

# Verificar
python -c "import openpyxl; import pandas; print('Excel MCP ready')"
```

### 7. context7, ddg-search, fetch

Estos MCPs son built-in desde el marketplace de Claude Code. No requieren instalación adicional.

### Zen MCP

El Zen MCP ya está incluido si tienes acceso a él. Verifica que las tools de Zen estén disponibles:

```
En Claude Code, escribe:
"¿Qué tools de Zen MCP tienes disponibles?"
```

## Verificación

### 1. Verificar Agentes

```
En Claude Code:
"Lista los agentes disponibles"
```

Deberías ver los 9 agentes.

### 2. Verificar MCPs

```
En Claude Code:
"¿Qué MCP servers tienes habilitados?"
```

Deberías ver memory, github, code-executor, playwright, etc.

### 3. Verificar Status Line

El status line debería mostrar:
- Nombre del modelo con color
- Directorio actual
- Barra de progreso de contexto
- Métricas de sesión (costo, duración, líneas)

### 4. Verificar Permisos

```
En Claude Code:
"Ejecuta: git status"
```

No debería pedir permiso (está en allow list).

### 5. Prueba de Agentes

```
En Claude Code:
"Escribe una función Python simple"
```

El agente `code-reviewer` debería activarse automáticamente después de escribir el código.

### 6. Prueba de MCPs

```
En Claude Code:
"Busca repositorios de Python en GitHub"
```

Debería usar el MCP `github` para buscar.

## Troubleshooting

### Problema: Los agentes no aparecen

**Solución**:
```bash
# Verificar que los archivos estén en el lugar correcto
# Windows
dir %USERPROFILE%\.claude\agents

# Linux/macOS
ls -la ~/.claude/agents/

# Verificar formato de archivos
cat ~/.claude/agents/code-reviewer.md
```

Los archivos deben tener frontmatter YAML válido:
```yaml
---
name: code-reviewer
description: ...
tools: Read, Write
model: sonnet
---
```

### Problema: El status line no funciona

**Solución**:
```bash
# Verificar Python
python --version

# Probar el script manualmente
python ~/.claude/scripts/context-monitor.py

# Verificar ruta en settings.local.json
cat ~/.claude/settings.local.json | grep statusLine

# Linux/macOS: Asegúrate de usar python3 si python apunta a Python 2
# Edita settings.local.json:
"command": "python3 .claude/scripts/context-monitor.py"
```

### Problema: MCPs no están disponibles

**Solución**:
```bash
# Verificar que estén habilitados
cat ~/.claude/settings.local.json | grep enabledMcpjsonServers

# Verificar instalación
npm list -g | grep playwright
deno --version
pip list | grep openpyxl

# Reiniciar Claude Code completamente
```

### Problema: Error de permisos

**Solución**:

Agrega el comando específico a `settings.local.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(tu-comando-aqui:*)"
    ]
  }
}
```

O configura modo ask:
```json
{
  "permissions": {
    "defaultMode": "ask"
  }
}
```

### Problema: Paths incorrectos (Windows/Linux)

**Solución**:

Ajusta todos los paths en `settings.local.json`:

**Windows**:
```json
"Bash(dir C:\\Users\\TU_USUARIO\\.claude\\agents)"
```

**Linux/macOS**:
```json
"Bash(ls /home/TU_USUARIO/.claude/agents)"
```

### Problema: GitHub token no funciona

**Solución**:
```bash
# Verificar que el token esté configurado
# Windows
echo %GITHUB_TOKEN%

# Linux/macOS
echo $GITHUB_TOKEN

# Si está vacío, configurar de nuevo
# Linux/macOS
export GITHUB_TOKEN="tu_token"

# Verificar scopes del token en GitHub:
# https://github.com/settings/tokens
# Debe tener: repo, workflow, write:packages
```

### Problema: Excel MCP no funciona

**Solución**:
```bash
# Reinstalar dependencias
pip install --upgrade openpyxl pandas xlsxwriter

# Verificar versiones
pip show openpyxl
pip show pandas

# Probar manualmente
python -c "import openpyxl; wb = openpyxl.Workbook(); print('OK')"
```

## Personalización Post-Instalación

### Deshabilitar MCPs no necesarios

Edita `settings.local.json`:

```json
{
  "enabledMcpjsonServers": [
    "memory",
    "github",
    "code-executor"
    // Comenta o elimina los que no necesites
  ]
}
```

### Modificar Comportamiento de Agentes

Edita los archivos `.md` en `~/.claude/agents/`:

```yaml
---
name: code-reviewer
description: Tu descripción personalizada
tools: Read, Write, Edit  # Agrega o quita tools
model: opus  # Cambia el modelo
---

Tu prompt personalizado aquí...
```

### Agregar Permisos Personalizados

Edita `settings.local.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(tu-comando-personalizado:*)",
      "mcp__tu-mcp-personalizado__*"
    ]
  }
}
```

## Siguientes Pasos

1. **Explora los agentes**: Prueba cada agente para familiarizarte
2. **Configura MCPs**: Instala solo los MCPs que necesites
3. **Personaliza**: Ajusta agentes y configuración a tu workflow
4. **Comparte**: Contribuye mejoras de vuelta al repositorio

## Soporte

Si encuentras problemas:

1. Revisa esta guía de troubleshooting
2. Consulta [docs/MCP_SERVERS.md](docs/MCP_SERVERS.md) para MCPs específicos
3. Abre un issue en GitHub con:
   - Sistema operativo
   - Versión de Claude Code
   - Logs de error
   - Pasos para reproducir

---

**¡Felicitaciones!** Tu configuración de Claude Code está lista.

Ver [README.md](README.md) para casos de uso y ejemplos.
