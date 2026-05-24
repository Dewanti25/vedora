const KEY = 'vedora_textbooks'

export function getTextbooks(){
  try{
    const raw = localStorage.getItem(KEY)
    return raw ? JSON.parse(raw) : []
  }catch(e){
    return []
  }
}

export function saveTextbooks(items){
  localStorage.setItem(KEY, JSON.stringify(items))
}

export function addTextbook(tb){
  const items = getTextbooks()
  const withId = {...tb, id: `tb_${Date.now()}`}
  items.unshift(withId)
  saveTextbooks(items)
  return items
}

export function updateTextbook(updated){
  const items = getTextbooks().map(b=> b.id === updated.id ? updated : b)
  saveTextbooks(items)
  return items
}

export function removeTextbook(id){
  const items = getTextbooks().filter(b=> b.id !== id)
  saveTextbooks(items)
  return items
}
