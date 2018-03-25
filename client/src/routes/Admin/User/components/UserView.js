import React from 'react'
import { Table, Icon, Divider } from 'antd'

const columns = [{
  title: '用户名',
  dataIndex: 'name',
  key: 'name',
  render: text => <a href="#">{ text }</a>,
}, {
  title: '手机',
  dataIndex: 'phone',
  key: 'phone',
}, {
  title: '邮箱',
  dataIndex: 'email',
  key: 'email',
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

const data = [{
  key: '1',
  name: 'John Brown',
  phone: 32,
  email: 'New York No. 1 Lake Park',
}, {
  key: '2',
  name: 'Jim Green',
  phone: 42,
  email: 'London No. 1 Lake Park',
}, {
  key: '3',
  name: 'Joe Black',
  phone: 32,
  email: 'Sidney No. 1 Lake Park',
}]

class UserView extends React.Component {
  render () {
    return (
      <div className="admin-user">
        <h2>用户管理 <Icon type="user"/></h2>
        <Table columns={ columns } dataSource={ data }/>
      </div>
    )
  }
}

export default UserView
