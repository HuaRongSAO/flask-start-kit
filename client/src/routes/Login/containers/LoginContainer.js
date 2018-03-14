import { connect } from 'react-redux'
import { increment, doubleAsync } from '../modules/LoginModules'
import LoginView from '../components/LoginView'

const mapDispatchToProps = {
  increment: () => increment(1),
  doubleAsync
}

const mapStateToProps = (state) => ({
  counter: state.counter
})

export default connect(mapStateToProps, mapDispatchToProps)(LoginView)
