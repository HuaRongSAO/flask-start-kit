// import { injectReducer } from './../../../store/reducers'
import UserView from './components/UserView'

export default (store) => ({
  path: 'user',
  getComponent (nextState, cb) {
    require.ensure([], (require) => {
      // const Counter = require('./containers/CounterContainer').default
      // const reducer = require('./modules/counter').default
      // injectReducer(store, {key: 'counter', reducer})
      cb(null, UserView)
    }, 'admin')
  }
})
