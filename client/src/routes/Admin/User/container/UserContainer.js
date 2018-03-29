import { connect } from 'react-redux'
import { getUsers } from './../modules/UserModule'
import UserView from './../components/UserView'

const mapDispatchToProps = {
  getUsers
}

const mapStateToProps = state => ({
  users: state.admin.users
})

export default connect(mapStateToProps, mapDispatchToProps)(UserView)
