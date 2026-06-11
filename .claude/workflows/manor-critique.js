export const meta = {
  name: 'manor-critique',
  description: 'Manor Protocol Critique gate - adversarial verification of a validation contract',
  whenToUse: 'Closing a mission milestone: verify every validation-contract assertion adversarially before Release.',
  phases: [
    { title: 'Contract', detail: 'load assertions' },
    { title: 'Verify', detail: 'one adversarial verifier per assertion' },
  ],
}

// args: { assertions?: [{id, statement, evidence?}], contractPath?: string }
const VERDICT = {
  type: 'object',
  properties: {
    satisfied: { type: 'boolean' },
    evidence: { type: 'string' },
    refutation: { type: 'string' },
  },
  required: ['satisfied', 'evidence'],
}

const CONTRACT = {
  type: 'object',
  properties: {
    assertions: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          statement: { type: 'string' },
          evidence: { type: 'string' },
        },
        required: ['id', 'statement'],
      },
    },
  },
  required: ['assertions'],
}

phase('Contract')
let assertions = Array.isArray(args && args.assertions) ? args.assertions : null
if (!assertions && args && args.contractPath) {
  const extracted = await agent(
    'Read the validation contract at ' + args.contractPath +
    ' and return its assertion list. Each assertion: id, the binary statement, declared evidence if stated.',
    { label: 'load-contract', phase: 'Contract', schema: CONTRACT }
  )
  assertions = extracted && extracted.assertions
}
if (!assertions || !assertions.length) {
  throw new Error('manor-critique requires args.assertions or args.contractPath')
}
log(assertions.length + ' assertions to verify')

phase('Verify')
const results = await pipeline(
  assertions,
  (a) => agent(
    'Manor Protocol Critique. You are an adversarial verifier in fresh context with no knowledge of the implementer.\n' +
    'Assertion ' + a.id + ': ' + a.statement + '\n' +
    'Declared evidence: ' + (a.evidence || 'none declared - gather your own') + '\n' +
    'Try to REFUTE the assertion. Run the declared evidence commands or inspect the named files yourself; ' +
    'do not trust claims you did not check. Set satisfied=true only if the evidence concretely holds. ' +
    'When uncertain, satisfied=false with the gap named in refutation.',
    { label: 'verify:' + a.id, phase: 'Verify', schema: VERDICT }
  ).then(v => ({ id: a.id, statement: a.statement, verdict: v })),
)

const clean = results.filter(Boolean)
const failed = clean.filter(r => !(r.verdict && r.verdict.satisfied))
log(failed.length ? failed.length + ' assertion(s) failed' : 'All assertions satisfied')

return {
  gate: failed.length === 0 && clean.length === assertions.length ? 'CLEAR' : 'BLOCKED',
  verified: clean.length,
  ofTotal: assertions.length,
  satisfied: clean.filter(r => r.verdict && r.verdict.satisfied).map(r => r.id),
  failed: failed.map(r => ({ id: r.id, statement: r.statement, refutation: (r.verdict && (r.verdict.refutation || r.verdict.evidence)) || 'verifier returned nothing' })),
}
