import {browserHistory} from 'react-router'
import { showLoading, hideLoading } from 'react-redux-loading-bar'
export const adminAuth = (store) => {
  store.dispatch(showLoading())
  // browserHistory.push('/login')
}
export default {adminAuth}
