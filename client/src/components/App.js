import React from 'react'
import { browserHistory, Router } from 'react-router'
import { Provider } from 'react-redux'
import PropTypes from 'prop-types'
import LoadingBar from 'react-redux-loading-bar'

class App extends React.Component {
  static propTypes = {
    store: PropTypes.object.isRequired,
    routes: PropTypes.array.isRequired,
  }

  shouldComponentUpdate () {
    return false
  }

  render () {
    return (
      <Provider store={this.props.store}>
        <div style={{height: '100%', minWidth: '1366px'}}>
          <LoadingBar  style={{ zIndex: '99' }}/>
          <Router history={browserHistory} children={this.props.routes}/>
        </div>
      </Provider>
    )
  }
}

export default App
