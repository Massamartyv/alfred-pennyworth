export const meta = {
  name: 'manor-recon',
  description: 'Manor Protocol Reconnaissance - survey territories, inventory the sources, synthesise a brief',
  whenToUse: 'Opening a Manor Protocol mission: fan researchers across territories, inventory the source set before fusing it, return one synthesis brief for the Direction gate.',
  phases: [
    { title: 'Survey', detail: 'one researcher per territory' },
    { title: 'Inventory', detail: 'build the source-inventory pack before synthesis' },
    { title: 'Synthesis', detail: 'merge reports into a mission brief' },
  ],
}

// args: { mission: string, territories?: string[] }
const mission = args && args.mission
if (!mission) throw new Error('manor-recon requires args.mission (string)')
const territories = Array.isArray(args.territories) && args.territories.length
  ? args.territories
  : ['the full scope of the mission']

phase('Survey')
log(`Surveying ${territories.length} territor${territories.length === 1 ? 'y' : 'ies'}`)
// Barrier is deliberate: the inventory needs every report at once.
const reports = (await parallel(territories.map(t => () =>
  agent(
    'Manor Protocol Reconnaissance. Mission: ' + mission + '\n' +
    'Your territory: ' + t + '\n' +
    'Survey the territory read-only. Do not modify anything. Report: current state, ' +
    'anomalies and divergences from documented intent, risks, opportunities and open questions. ' +
    'Inventory every source you touch - path, type, apparent date, apparent authority, and whether it ' +
    'looks current or superseded. Flag contradictions between sources, references to material you ' +
    'cannot find, and suspected duplicate or near-duplicate files. ' +
    'Concrete file paths and evidence over generalities. Raw findings, no preamble.',
    { label: 'survey:' + String(t).slice(0, 40), phase: 'Survey' }
  )
))).filter(Boolean)

if (!reports.length) throw new Error('No territory reports returned')

phase('Inventory')
// Inventory before synthesis: make the source set legible so synthesis cannot smooth conflicts.
const inventory = await agent(
  'Manor Protocol Reconnaissance - source inventory. Mission: ' + mission + '\n' +
  'Build the source-inventory pack per Agents/templates/source-inventory.md from the territory ' +
  'reports below. Produce four sections and nothing else: ' +
  '(1) Source Inventory - every source with path, type, date, authority ' +
  '[authoritative | supporting | background | superseded], status and intended use; ' +
  '(2) Conflict Log - claims in tension between sources, with a recommended handling but no resolution; ' +
  '(3) Missing-Context List - material referenced but absent, and why it matters; ' +
  '(4) Duplicates Report - suspected version families with a confidence level. ' +
  'Surface, do not resolve. Do not delete or rank away any source. ' +
  'Cite source paths throughout.\n\n' +
  reports.map((r, i) => '=== Report ' + (i + 1) + ': ' + territories[i] + ' ===\n' + r).join('\n\n'),
  { label: 'inventory', phase: 'Inventory' }
)

phase('Synthesis')
const brief = await agent(
  'Manor Protocol Reconnaissance synthesis. Mission: ' + mission + '\n' +
  'Using the reviewed source inventory below as the working set, merge the territory reports into one ' +
  'mission brief with four sections: (1) state of play, (2) gaps and liabilities ranked by severity, ' +
  '(3) open questions for the Direction gate, (4) recommended scope. ' +
  'Treat the conflict log and missing-context list as unresolved inputs to raise at Direction - ' +
  'carry them forward, do not smooth them over. Mark any claim that rests on a superseded or ' +
  'conflicted source. Cite source evidence throughout.\n\n' +
  '=== Source Inventory ===\n' + inventory + '\n\n' +
  reports.map((r, i) => '=== Report ' + (i + 1) + ': ' + territories[i] + ' ===\n' + r).join('\n\n'),
  { label: 'synthesis', phase: 'Synthesis' }
)

return { mission, territories, inventory, brief }
