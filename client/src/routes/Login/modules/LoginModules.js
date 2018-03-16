export const LOGIN = 'LOGIN'

// ------------------------------------
// Actions
// ------------------------------------
export function login (access_token) {
  return {
    type: LOGIN,
    payload: {access_token}
  }
}

export const loginAsync = (user) => {
  return (dispatch, getState) => {
    async () => {
      const {data} = await api.post('/api/auth', user)
      localStorage.setItem('access_token', data.access_token)
      dispatch({
        type: LOGIN,
        payload: data.access_token
      })
    }
  }
}

export const actions = {
  login,
  loginAsync
}

// ------------------------------------
// Action Handlers
// ------------------------------------
const ACTION_HANDLERS = {
  [LOGIN]: (state, action) => (state.access_token = action.payload.access_token)
}

// ------------------------------------
// Reducer
// ------------------------------------
const initialState = {
  access_token: ''
}

export default function loginReducer (state = initialState, action) {
  const handler = ACTION_HANDLERS[action.type]
  return handler ? handler(state, action) : state
}
