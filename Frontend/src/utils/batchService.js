const KEY = 'vedora_batches'

export function getBatches(){
  try{
    const raw = localStorage.getItem(KEY)
    return raw ? JSON.parse(raw) : []
  }catch(e){
    return []
  }
}

export function saveBatches(items){
  localStorage.setItem(KEY, JSON.stringify(items))
}

export function addBatch(batch){
  const items = getBatches()
  const withId = {...batch, id: `batch_${Date.now()}`}
  items.unshift(withId)
  saveBatches(items)
  return items
}

export function updateBatch(updated){
  const items = getBatches().map(b=> b.id === updated.id ? updated : b)
  saveBatches(items)
  return items
}

export function removeBatch(id){
  const items = getBatches().filter(b=> b.id !== id)
  saveBatches(items)
  return items
}
