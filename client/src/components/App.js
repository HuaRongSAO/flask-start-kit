import React from 'react'
import { browserHistory, Router } from 'react-router'
import { Provider, connect } from 'react-redux'
import PropTypes from 'prop-types'
import { updateAuth, exitAuth } from './../store/auth'

class App extends React.Component {
  static PropTypes = {
    store: PropTypes.object.isRequired,
    routes: PropTypes.array.isRequired,
  }

  shouldComponentUpdate () {
    return false
  }

  componentWillMount = async () => {
    const {exitAuth, updateAuth} = this.props
    const accessToken = localStorage.getItem('access_token')
    if (!accessToken) return exitAuth()
    const {data} = await api.get('/api/auth/login')
    updateAuth(data)
  }

  render () {
    return (
      <Provider store={this.props.store}>
        <div style={{height: '100%', minWidth: '1366px'}}>
          <Router history={browserHistory} children={this.props.routes}/>
        </div>
      </Provider>
    )
  }
}

const mapDispatchToProps = {updateAuth, exitAuth}
const mapStateToProps = (state) => ({})
export default connect(mapStateToProps, mapDispatchToProps)(App)
