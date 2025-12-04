# Variables de Entorno

Documentación de todas las variables de entorno configuradas y disponibles en esta configuración.

## Variables Configuradas

### CLAUDE_CODE_MAX_OUTPUT_TOKENS

**Valor**: `8000`
**Propósito**: Aumenta el límite de tokens de salida de Claude Code
**Por defecto**: Aproximadamente 4096 tokens

**Beneficios**:
- Respuestas más largas y completas
- Permite generar archivos más grandes en una sola respuesta
- Mejor para documentación extensa o código complejo

**Cuándo cambiar**:
- Reducir si experimentas timeouts
- Aumentar si necesitas respuestas aún más largas

---

### DISABLE_NON_ESSENTIAL_MODEL_CALLS

**Valor**: `1`
**Propósito**: Desactiva llamadas no esenciales al modelo para reducir costos

**Efectos**:
- Reduce llamadas redundantes
- Optimiza uso de API
- Puede hacer respuestas ligeramente menos refinadas

**Cuándo desactivar** (configurar a `0`):
- Si experimentas respuestas de menor calidad
- Si el costo no es una preocupación

---

### DISABLE_COST_WARNINGS

**Valor**: `1`
**Propósito**: Desactiva advertencias de costo en la interfaz

**Efectos**:
- Interfaz más limpia
- No interrumpe el flujo de trabajo
- No afecta el tracking real de costos

**Cuándo desactivar** (configurar a `0`):
- Si quieres ser muy consciente de los costos
- Para proyectos con presupuesto limitado

---

## Variables Requeridas por MCPs

Estas variables son necesarias para ciertos MCP servers:

### GITHUB_TOKEN

**Requerido por**: MCP github
**Cómo obtener**:
1. Ve a https://github.com/settings/tokens
2. Click en "Generate new token (classic)"
3. Selecciona scopes: `repo`, `workflow`, `write:packages`
4. Copia el token

**Configurar**:
```bash
# Windows
setx GITHUB_TOKEN "ghp_tu_token_aqui"

# Linux/macOS
echo 'export GITHUB_TOKEN="ghp_tu_token_aqui"' >> ~/.bashrc
source ~/.bashrc
```

---

### POSTGRES_CONNECTION

**Requerido por**: MCP postgresql
**Formato**: `postgresql://usuario:password@host:puerto/database`

**Ejemplo**:
```
postgresql://myuser:mypassword@localhost:5432/mydatabase
```

**Configurar**:
```bash
# Windows
setx POSTGRES_CONNECTION "postgresql://user:pass@localhost:5432/db"

# Linux/macOS
echo 'export POSTGRES_CONNECTION="postgresql://user:pass@localhost:5432/db"' >> ~/.bashrc
source ~/.bashrc
```

---

### ANTHROPIC_API_KEY

**Requerido por**: Claude Code (ya configurado)
**Cómo obtener**: Desde tu cuenta de Anthropic

**Nota**: Esta variable ya debería estar configurada si Claude Code funciona.

---

## Configuración en settings.local.json

Las variables de entorno se configuran en `settings.local.json`:

```json
{
  "env": {
    "CLAUDE_CODE_MAX_OUTPUT_TOKENS": "8000",
    "DISABLE_NON_ESSENTIAL_MODEL_CALLS": "1",
    "DISABLE_COST_WARNINGS": "1",
    "GITHUB_TOKEN": "${GITHUB_TOKEN}",
    "POSTGRES_CONNECTION": "${POSTGRES_CONNECTION}"
  }
}
```

**Nota**: Usa `${VARIABLE}` para referenciar variables del sistema operativo.

## Variables Opcionales

### DEBUG

**Valor**: `1` para activar, `0` o no definida para desactivar
**Propósito**: Activa logging detallado

```json
{
  "env": {
    "DEBUG": "1"
  }
}
```

---

### LOG_LEVEL

**Valores**: `debug`, `info`, `warn`, `error`
**Propósito**: Controla nivel de logging

```json
{
  "env": {
    "LOG_LEVEL": "debug"
  }
}
```

---

### DENO_DIR

**Propósito**: Directorio de caché de Deno para code-executor MCP
**Por defecto**: `~/.deno`

```json
{
  "env": {
    "DENO_DIR": "/custom/path/to/deno/cache"
  }
}
```

---

## Verificación de Variables

### Windows

```powershell
# Ver todas las variables de entorno
Get-ChildItem Env:

# Ver variable específica
echo $env:GITHUB_TOKEN
echo $env:CLAUDE_CODE_MAX_OUTPUT_TOKENS
```

### Linux/macOS

```bash
# Ver todas las variables
printenv

# Ver variable específica
echo $GITHUB_TOKEN
echo $CLAUDE_CODE_MAX_OUTPUT_TOKENS
```

### Desde Claude Code

Puedes pedirle a Claude que verifique:

```
"¿Qué variables de entorno tienes configuradas?"
```

## Seguridad

### ⚠️ IMPORTANTE: Protección de Credenciales

**NUNCA** pongas credenciales directamente en `settings.local.json`:

```json
// ❌ MAL
{
  "env": {
    "GITHUB_TOKEN": "ghp_1234567890abcdef"
  }
}

// ✅ BIEN
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

### Mejores Prácticas

1. **Usa variables del sistema**: Configura credenciales en el sistema operativo
2. **Archivo .env**: Usa archivos `.env` (excluidos del git)
3. **Git ignore**: Nunca hagas commit de credenciales
4. **Rotación**: Rota tokens regularmente
5. **Scope mínimo**: Da solo los permisos necesarios

### Verificar antes de Commit

```bash
# Buscar posibles credenciales
grep -r "api_key\|token\|password" config/

# Ver cambios antes de commit
git diff

# Si encuentras credenciales, NO hagas commit
```

## Troubleshooting

### Variable no se carga

**Problema**: La variable configurada no está disponible

**Soluciones**:
```bash
# 1. Reinicia Claude Code completamente

# 2. Verifica sintaxis en settings.local.json
cat ~/.claude/settings.local.json

# 3. Verifica que la variable existe en el sistema
# Windows
echo %GITHUB_TOKEN%

# Linux/macOS
echo $GITHUB_TOKEN

# 4. Recargar variables de entorno
# Windows: Cerrar y abrir nuevo terminal
# Linux/macOS
source ~/.bashrc
```

### Variable con valor incorrecto

**Problema**: La variable tiene un valor diferente al esperado

**Solución**:
```bash
# Verificar orden de precedencia:
# 1. settings.local.json env
# 2. Variables del sistema
# 3. Variables de shell

# Depurar en Claude Code
"Ejecuta: echo $VARIABLE_NAME"
```

### MCP no encuentra credencial

**Problema**: MCP reporta error de autenticación

**Solución**:
```bash
# Verificar que el nombre coincida exactamente
# El MCP espera: GITHUB_TOKEN
# No: Github_Token, github_token, etc.

# Verificar formato
# PostgreSQL requiere: postgresql://...
# No: postgres://... (sin 'ql')

# Verificar scopes del token (GitHub)
# Ve a: https://github.com/settings/tokens
```

## Personalización

### Agregar Nueva Variable

1. Configura en el sistema:
```bash
# Linux/macOS
export MI_VARIABLE="mi_valor"
echo 'export MI_VARIABLE="mi_valor"' >> ~/.bashrc
```

2. Referencia en settings.local.json:
```json
{
  "env": {
    "MI_VARIABLE": "${MI_VARIABLE}"
  }
}
```

3. Reinicia Claude Code

### Valores por Entorno

Puedes tener diferentes valores según el entorno:

```json
{
  "env": {
    "API_URL": "${NODE_ENV == 'production' ? 'https://api.prod.com' : 'https://api.dev.com'}"
  }
}
```

---

Para más información:
- [MCP_SERVERS.md](MCP_SERVERS.md) - Variables específicas de MCPs
- [INSTALLATION.md](../INSTALLATION.md) - Guía de instalación
- [README.md](../README.md) - Documentación general
