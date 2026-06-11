export const meta = {
  name: 'manor-recon',
  description: 'Manor Protocol Reconnaissance - parallel territory survey and synthesis',
  whenToUse: 'Opening a Manor Protocol mission: fan researchers across territories, return one synthesis brief for the Direction gate.',
  phases: [
    { title: 'Survey', detail: 'one researcher per territory' },
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
// Barrier is deliberate: synthesis needs every report at once.
const reports = (await parallel(territories.map(t => () =>
  agent(
    'Manor Protocol Reconnaissance. Mission: ' + mission + '\n' +
    'Your territory: ' + t + '\n' +
    'Survey the territory read-only. Do not modify anything. Report: current state, ' +
    'anomalies and divergences from documented intent, risks, opportunities and open questions. ' +
    'Concrete file paths and evidence over generalities. Raw findings, no preamble.',
    { label: 'survey:' + String(t).slice(0, 40), phase: 'Survey' }
  )
))).filter(Boolean)

if (!reports.length) throw new Error('No territory reports returned')

phase('Synthesis')
const brief = await agent(
  'Manor Protocol Reconnaissance synthesis. Mission: ' + mission + '\n' +
  'Merge the territory reports below into one mission brief with four sections: ' +
  '(1) state of play, (2) gaps and liabilities ranked by severity, ' +
  '(3) open questions for the Direction gate, (4) recommended scope. ' +
  'Cite territory evidence throughout.\n\n' +
  reports.map((r, i) => '=== Report ' + (i + 1) + ': ' + territories[i] + ' ===\n' + r).join('\n\n'),
  { label: 'synthesis', phase: 'Synthesis' }
)

return { mission, territories, brief }
