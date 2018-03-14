// Sync route definition
export default (store) => ({
  getComponent (nextState, cb) {
    require.ensure([], (require) => {
      const LoginView = require('./components/LoginView').default
      cb(null, LoginView)
    }, 'login')
  }
})
