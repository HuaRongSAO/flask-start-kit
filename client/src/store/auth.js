// ------------------------------------
// Constants
// ------------------------------------
export const EXIT = 'EXIT'
export const AUTH = 'AUTH'
// ------------------------------------
// Actions
// ------------------------------------
export function exit () {
  return {
    type: EXIT
  }
}

export function auth (user) {
  return {
    type: AUTH,
    payload: {user}
  }
}

// ------------------------------------
// Specialized Action Creator
// ------------------------------------
export const updateAuth = ({dispatch}) => {
  return user => dispatch(auth(user))
}
export const exitAuth = ({dispatch}) => {
  return () => dispatch(exit())
}

// ------------------------------------
// Action Handlers
// ------------------------------------
const ACTION_HANDLERS = {
  [AUTH]: (state, action) => ({user: {...action.payload.user, load: true}}),
  [EXIT]: (state, action) => ({user: {load: false}})
}

// ------------------------------------
// Reducer
// ------------------------------------
const initialState = {
  user: {load: false}
}

export default function loginReducer (state = initialState, action) {
  const handler = ACTION_HANDLERS[action.type]
  return handler ? handler(state, action) : state
}
