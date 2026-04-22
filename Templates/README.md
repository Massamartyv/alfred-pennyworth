# Templates

Reusable project templates and methodology artefacts. Start points for recurring work patterns, cloned into the target destination and adapted.

## Structure

```
Templates/
├── Website/                       -- Web development templates
│   └── nextjs-starter/             -- Next.js 16 starter scaffolded for Five Points client builds
├── spring-cleaning-prompt.md       -- Architectural audit methodology used for the nine-lane sweep
```

## Current Templates

| Template | Purpose | Used By |
|---|---|---|
| `Website/nextjs-starter/` | Next.js 16 App Router scaffold with TypeScript, CSS Modules, and Five Points conventions. Cloned into each new Five Points client engagement. | Five Points Production studio |
| `spring-cleaning-prompt.md` | The architectural-audit methodology that launches a nine-lane parallel sweep of the Alfred Pennyworth repository. Invoked on a cadence or when the repo feels out of alignment. | System-level maintenance |

## Adding a New Template

1. Create the template folder (Title Case) at the appropriate subdirectory (`Templates/Website/`, `Templates/{Category}/`) or at the root for methodology files
2. Include a README in the template root that describes what the template is, when to use it and the clone-and-adapt workflow
3. Keep templates generic – hard-coded client names, account identifiers or secrets should never live in a template
4. When cloning a template into a venture, copy the folder, rename it, and update any placeholders

## Conventions

- **Folder naming:** Title Case for categories (`Website/`), kebab-case or Title Case for specific templates based on domain convention
- **Stack-specific templates** live in subfolders by stack (`Website/`, `Python/`, etc.)
- **Methodology files** live at the root (`spring-cleaning-prompt.md`)
- **Client-specific adaptations** are not templates – they belong in the client folder under the relevant venture
