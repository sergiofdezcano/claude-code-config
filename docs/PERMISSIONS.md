# Sistema de Permisos

Documentación completa del sistema de permisos de Claude Code y cómo está configurado en esta setup.

## Tabla de Contenidos

- [Conceptos Básicos](#conceptos-básicos)
- [Modos de Permiso](#modos-de-permiso)
- [Permisos Configurados](#permisos-configurados)
- [Sintaxis de Permisos](#sintaxis-de-permisos)
- [Mejores Prácticas](#mejores-prácticas)

## Conceptos Básicos

Claude Code usa un sistema de permisos para controlar qué operaciones puede realizar sin pedir confirmación al usuario.

### Tres Listas

1. **allow**: Operaciones permitidas sin confirmación
2. **deny**: Operaciones bloqueadas completamente
3. **ask**: Operaciones que requieren confirmación

### Archivo de Configuración

Los permisos se definen en dos archivos:

- `settings.json`: Permisos básicos
- `settings.local.json`: Permisos adicionales y específicos del entorno

## Modos de Permiso

### defaultMode

Controla el comportamiento por defecto para operaciones no listadas:

```json
{
  "permissions": {
    "defaultMode": "ask"  // Opciones: "allow", "deny", "ask"
  }
}
```

| Modo | Comportamiento |
|------|----------------|
| `ask` | Pregunta al usuario (recomendado) |
| `allow` | Permite todo por defecto (peligroso) |
| `deny` | Deniega todo por defecto (restrictivo) |

## Permisos Configurados

### settings.json - Permisos Básicos

```json
{
  "permissions": {
    "allow": [
      "Bash(mkdir:*)",
      "Bash(tree:*)",
      "Bash(git init:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(git config:*)",
      "Bash(gh repo create:*)",
      "Bash(git push:*)",
      "Bash(git mv:*)"
    ],
    "deny": [],
    "ask": [],
    "defaultMode": "ask"
  }
}
```

**Operaciones permitidas**:
- ✅ Crear directorios (`mkdir`)
- ✅ Ver árbol de archivos (`tree`)
- ✅ Operaciones git básicas (init, add, commit, push)
- ✅ Crear repositorios con GitHub CLI (`gh repo create`)

### settings.local.json - Permisos Extendidos

```json
{
  "permissions": {
    "allow": [
      "WebFetch(domain:github.com)",
      "WebFetch(domain:raw.githubusercontent.com)",
      "Bash(dir:*)",
      "Bash(powershell:*)",
      "Bash(npm install:*)",
      "Bash(pip install:*)",
      "Bash(cat:*)",
      "Bash(copy:*)",
      "mcp__code-executor__health",
      "mcp__code-executor__executeTypescript",
      "mcp__github__search_repositories",
      "WebSearch"
    ]
  }
}
```

**Operaciones adicionales**:
- ✅ Fetch de GitHub y GitHub raw
- ✅ Comandos de shell (dir, powershell)
- ✅ Instalación de paquetes (npm, pip)
- ✅ Lectura y copia de archivos
- ✅ MCPs específicos (code-executor, github)
- ✅ Búsqueda web

## Sintaxis de Permisos

### Formato General

```
ToolName(param1:value1, param2:value2)
```

### Wildcards

Usa `*` para permitir cualquier valor:

```json
"Bash(mkdir:*)"        // mkdir con cualquier argumento
"Bash(git add:*)"      // git add con cualquier archivo
"mcp__github__*"       // Todas las tools del MCP github
```

### Ejemplos por Tool

#### Bash

```json
"Bash(comando:*)"              // Comando específico con cualquier arg
"Bash(git status:*)"           // Git status
"Bash(npm install:*)"          // NPM install cualquier paquete
"Bash(python script.py:*)"    // Ejecutar script Python
```

#### WebFetch

```json
"WebFetch(domain:github.com)"           // Solo GitHub
"WebFetch(domain:api.example.com)"      // API específica
"WebFetch(domain:*.github.com)"         // Subdominios de GitHub
```

#### MCPs

```json
"mcp__servidor__tool"                   // Tool específico
"mcp__servidor__*"                      // Todas las tools del servidor
"mcp__github__search_repositories"      // Solo búsqueda de repos
"mcp__code-executor__executeTypescript" // Solo ejecución de código
```

#### Read/Write/Edit

```json
"Read(path:/specific/path/*)"       // Leer archivos en path específico
"Write(path:/output/*)"             // Escribir en directorio output
"Edit(path:/src/*)"                 // Editar archivos en src
```

### Permisos Compuestos

Puedes combinar múltiples condiciones:

```json
"Bash(git commit:*, --no-verify:false)"  // Commit sin skip hooks
```

## Permisos por Categoría

### Git Operations

```json
{
  "allow": [
    "Bash(git status:*)",
    "Bash(git diff:*)",
    "Bash(git log:*)",
    "Bash(git add:*)",
    "Bash(git commit:*)",
    "Bash(git push:*)",
    "Bash(git pull:*)",
    "Bash(git checkout:*)",
    "Bash(git branch:*)"
  ]
}
```

### File Operations

```json
{
  "allow": [
    "Bash(mkdir:*)",
    "Bash(cat:*)",
    "Bash(ls:*)",
    "Bash(dir:*)",
    "Bash(copy:*)",
    "Bash(cp:*)",
    "Bash(mv:*)",
    "Read(path:*)",
    "Write(path:/safe/directory/*)"
  ]
}
```

### Package Management

```json
{
  "allow": [
    "Bash(npm install:*)",
    "Bash(npm run:*)",
    "Bash(pip install:*)",
    "Bash(cargo build:*)",
    "Bash(go mod download:*)"
  ]
}
```

### MCPs Comunes

```json
{
  "allow": [
    "mcp__github__*",
    "mcp__memory__*",
    "mcp__code-executor__executeTypescript",
    "mcp__context7__*",
    "WebSearch"
  ]
}
```

## Mejores Prácticas

### 1. Principio de Mínimo Privilegio

Solo permite lo estrictamente necesario:

```json
// ❌ Demasiado permisivo
"Bash(*:*)"

// ✅ Específico
"Bash(git status:*)",
"Bash(git diff:*)"
```

### 2. Usa defaultMode: "ask"

Esto permite que Claude pida permiso para operaciones no listadas:

```json
{
  "permissions": {
    "defaultMode": "ask"
  }
}
```

### 3. Separa Permisos por Entorno

- `settings.json`: Permisos universales seguros
- `settings.local.json`: Permisos específicos del proyecto

### 4. Revisa Regularmente

Audita periódicamente los permisos:

```bash
# Ver permisos actuales
cat ~/.claude/settings.json
cat ~/.claude/settings.local.json

# Buscar permisos con wildcards
grep -n "\*" ~/.claude/settings*.json
```

### 5. Documenta Permisos Personalizados

Si agregas permisos, documenta por qué:

```json
{
  "allow": [
    // Permite instalar paquetes para desarrollo
    "Bash(npm install:*)",

    // Acceso a API de GitHub para CI/CD
    "mcp__github__*"
  ]
}
```

### 6. Operaciones Peligrosas en "ask"

Nunca permitas automáticamente:

```json
{
  "ask": [
    "Bash(rm:*)",           // Eliminación de archivos
    "Bash(sudo:*)",         // Comandos con sudo
    "Bash(chmod:*)",        // Cambios de permisos
    "Bash(git push --force:*)"  // Force push
  ]
}
```

## Seguridad

### Operaciones de Alto Riesgo

**NUNCA permitas sin confirmación**:

```json
// ❌ PELIGROSO
{
  "allow": [
    "Bash(rm:*)",
    "Bash(sudo:*)",
    "Bash(dd:*)",
    "Bash(mkfs:*)",
    "Bash(git push --force:*)"
  ]
}
```

### Límites de Path

Restringe acceso a paths específicos:

```json
{
  "allow": [
    "Read(path:/proyecto/*)",        // Solo leer en /proyecto
    "Write(path:/proyecto/output/*)" // Solo escribir en /proyecto/output
  ],
  "deny": [
    "Read(path:/etc/*)",      // Bloquear lectura de config sistema
    "Write(path:/system/*)",  // Bloquear escritura en sistema
    "Bash(rm:/home/*)"        // Bloquear rm en home
  ]
}
```

### Dominios de Red

Limita acceso a dominios conocidos:

```json
{
  "allow": [
    "WebFetch(domain:github.com)",
    "WebFetch(domain:api.openai.com)",
    "WebFetch(domain:docs.anthropic.com)"
  ],
  "deny": [
    "WebFetch(domain:*.suspicious-site.com)"
  ]
}
```

## Troubleshooting

### Permiso Denegado

**Problema**: Claude dice que no tiene permiso para una operación

**Solución**:
1. Identifica el comando exacto:
   ```
   Error: Permission denied for Bash(git push origin main)
   ```

2. Agrégalo a allow:
   ```json
   {
     "allow": [
       "Bash(git push:*)"
     ]
   }
   ```

3. Reinicia Claude Code

### Permiso Muy Amplio

**Problema**: Has dado demasiados permisos

**Solución**:
1. Identifica permisos amplios:
   ```bash
   grep "\*:\*" ~/.claude/settings*.json
   ```

2. Reemplaza con permisos específicos:
   ```json
   // Antes
   "Bash(*:*)"

   // Después
   "Bash(git status:*)",
   "Bash(git diff:*)",
   "Bash(git add:*)"
   ```

### Claude Pide Permiso Constantemente

**Problema**: Claude pide confirmación para todo

**Solución**:

Opción 1 - Agregar comandos frecuentes a allow:
```json
{
  "allow": [
    "Bash(ls:*)",
    "Bash(cat:*)",
    "Read(path:*)"
  ]
}
```

Opción 2 - Cambiar defaultMode temporalmente:
```json
{
  "permissions": {
    "defaultMode": "allow"  // Solo para desarrollo
  }
}
```

⚠️ **Advertencia**: Vuelve a "ask" después del desarrollo.

## Ejemplos de Configuración

### Desarrollo Web

```json
{
  "permissions": {
    "allow": [
      "Bash(npm:*)",
      "Bash(yarn:*)",
      "Bash(git:*)",
      "Bash(node:*)",
      "Read(path:./src/*)",
      "Write(path:./src/*)",
      "Write(path:./dist/*)",
      "WebFetch(domain:api.github.com)",
      "mcp__github__*"
    ],
    "defaultMode": "ask"
  }
}
```

### Data Science

```json
{
  "permissions": {
    "allow": [
      "Bash(python:*)",
      "Bash(pip:*)",
      "Bash(jupyter:*)",
      "Read(path:./data/*)",
      "Write(path:./output/*)",
      "mcp__postgresql__*",
      "mcp__excel__*"
    ],
    "defaultMode": "ask"
  }
}
```

### DevOps

```json
{
  "permissions": {
    "allow": [
      "Bash(docker:*)",
      "Bash(kubectl:*)",
      "Bash(terraform:*)",
      "Bash(git:*)",
      "mcp__github__*",
      "WebFetch(domain:api.*.cloud)"
    ],
    "ask": [
      "Bash(terraform apply:*)",
      "Bash(kubectl delete:*)"
    ],
    "defaultMode": "ask"
  }
}
```

---

Para más información:
- [INSTALLATION.md](../INSTALLATION.md) - Guía de instalación
- [ENVIRONMENT_VARIABLES.md](ENVIRONMENT_VARIABLES.md) - Variables de entorno
- [README.md](../README.md) - Documentación general
