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
export const updateAuth = user => {
  return dispatch => dispatch(auth(user))
}
export const exitAuth = () => {
  return dispatch => dispatch(exit())
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
