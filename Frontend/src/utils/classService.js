const KEY = 'vedora_joined_classes'

export function getJoinedClasses(){
  try{
    const raw = localStorage.getItem(KEY)
    return raw ? JSON.parse(raw) : []
  }catch(e){
    return []
  }
}

export function saveJoinedClasses(items){
  localStorage.setItem(KEY, JSON.stringify(items))
}

export function addJoinedClass(batch){
  const items = getJoinedClasses()
  if(items.find(i=> i.id === batch.id)) return items
  if(batch.current >= batch.max) return items
  const copy = [...items, batch]
  saveJoinedClasses(copy)
  return copy
}

export function removeJoinedClass(id){
  const items = getJoinedClasses().filter(i=> i.id !== id)
  saveJoinedClasses(items)
  return items
}

export function isJoined(id){
  return getJoinedClasses().some(i=> i.id === id)
}
