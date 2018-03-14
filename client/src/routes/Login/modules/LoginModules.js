
export const ASYNC_LOGIN = 'ASYNC_LOGIN'

// ------------------------------------
// Actions
// ------------------------------------
export function login (user = {username: '', password: '', remember: true}) {
  return {
    type: ASYNC_LOGIN,
    payload: user
  }
}

/*  This is a thunk, meaning it is a function that immediately
    returns a function for lazy evaluation. It is incredibly useful for
    creating async actions, especially when combined with redux-thunk! */

export const loginAsync = () => {
  return async (dispatch, getState) => {
    const {data} = await api.get('/api/user')
    console.log(data)
    const user = getState().user
    dispatch({
      type: ASYNC_LOGIN,
      payload: user
    })
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
  [ASYNC_LOGIN]: (state, action) => state + action.payload,
}

// ------------------------------------
// Reducer
// ------------------------------------
const initialState = 0

export default function loginReducer (state = initialState, action) {
  const handler = ACTION_HANDLERS[action.type]
  return handler ? handler(state, action) : state
}
