const KEY = 'vedora_syllabus_plans'

export function getPlans(){
  try{ const raw = localStorage.getItem(KEY); return raw? JSON.parse(raw): [] }catch(e){return []}
}

export function savePlans(items){
  localStorage.setItem(KEY, JSON.stringify(items))
}

export function addPlan(plan){
  const items = getPlans()
  const withId = {...plan, id: `plan_${Date.now()}`}
  items.unshift(withId)
  savePlans(items)
  return items
}

export function updatePlan(plan){
  const items = getPlans().map(p=> p.id===plan.id? plan: p)
  savePlans(items)
  return items
}

export function removePlan(id){
  const items = getPlans().filter(p=> p.id !== id)
  savePlans(items)
  return items
}
