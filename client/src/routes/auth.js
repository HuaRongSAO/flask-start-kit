export const adminAuth = store => (nextState, replace) => {
  if (!localStorage.getItem('access_token')) return replace('/login')
}
export default {adminAuth}
