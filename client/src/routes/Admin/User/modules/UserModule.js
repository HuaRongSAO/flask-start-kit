export const ASYNC_USERS = 'ASYNC_USERS'

// ------------------------------------
// Actions
// ------------------------------------

export const getUsers = (page_index = 0, page_size = 10) => async (dispatch, getState) => {
  const {data} = await api.get('/api/user').catch(() => false)
  dispatch({
    type: ASYNC_USERS,
    payload: data
  })
}

export const actions = {
  getUsers
}

// ------------------------------------
// Action Handlers
// ------------------------------------
const ACTION_HANDLERS = {
  [ASYNC_USERS]: (state, action) => ({...state, users: action.payload})
}

// ------------------------------------
// Reducer
// ------------------------------------
const initialState = {
  users: {count: 0, list: []}
}

export default function loginReducer (state = initialState, action) {
  const handler = ACTION_HANDLERS[action.type]
  return handler ? handler(state, action) : state
}
