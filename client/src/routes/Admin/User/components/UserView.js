import React from 'react'
import { Tooltip, Table, Icon, Divider } from 'antd'

const columns = [{
  title: 'ID',
  dataIndex: 'id',
  key: 'id'
}, {
  title: '用户名',
  dataIndex: 'username',
  key: 'username',
  render: text => <Tooltip placement="top" title={ text }>
    <a href="javascript:void 0">{ text }</a></Tooltip>,
}, {
  title: '手机',
  dataIndex: 'phone',
  key: 'phone',
}, {
  title: '邮箱',
  dataIndex: 'email',
  key: 'email',
}, {
  title: '创建时间',
  dataIndex: 'create_time',
  key: 'create_time'
}, {
  title: '管理',
  key: 'action',
  render: (text, record) => (
    <span>
      <a href="#">修改</a>
      <Divider type="vertical"/>
      <a href="#">删除</a>
    </span>
  ),
}]

class UserView extends React.Component {
  componentWillMount () {
    this.props.getUsers()
  }
  
  render () {
    const {list} = this.props.users
    return (
      <div className="admin-user">
        <h2>用户管理 <Icon type="user"/></h2>
        <Table columns={ columns } dataSource={ list } rowKey={ 'id' }/>
      </div>
    )
  }
}

export default UserView
