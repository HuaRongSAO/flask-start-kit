import { connect } from 'react-redux'
import { login, loginAsync } from '../modules/LoginModules'
import LoginView from '../components/LoginView'

const mapDispatchToProps = {
  login,
  loginAsync
}

const mapStateToProps = (state) => ({
  counter: state.counter
})

export default connect(mapStateToProps, mapDispatchToProps)(LoginView)
