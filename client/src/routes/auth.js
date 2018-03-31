
export const adminAuth = (nextState, replace) => {
  if (!localStorage.getItem('access_token')) return replace('/login')
  api.get('/api/auth/login').catch(() => {return replace('/login')})
}
export default {adminAuth}
