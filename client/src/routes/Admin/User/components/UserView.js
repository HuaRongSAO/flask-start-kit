import React from 'react'
import { Tooltip, Table, Icon, Divider, Button, Modal } from 'antd'
import './UserView.scss'
const columns = [{title: 'ID', dataIndex: 'id', key: 'id'},
  {
    title: '用户名', dataIndex: 'username', key: 'username',
    render: text => <Tooltip placement="top" title={text}> <a href="javascript:void 0">{text}</a></Tooltip>,
  },
  {title: '手机', dataIndex: 'phone', key: 'phone'},
  {title: '邮箱', dataIndex: 'email', key: 'email'},
  {title: '创建时间', dataIndex: 'create_time', key: 'create_time'},
  {
    title: '管理',
    key: 'action',
    render: (text, record) => ( <span><a href="#">修改</a><Divider type="vertical"/><a href="#">删除</a></span>),
  }
]

class UserView extends React.Component {
  componentWillMount () {
    this.props.getUsers()
  }

  state = {visible: false, loading: false,}
  showModal = () => {
    this.setState({
      visible: true,
    })
  }
  handleOk = (e) => {
    console.log(e)
    this.setState({
      visible: false,
    })
  }
  handleCancel = (e) => {
    console.log(e)
    this.setState({
      visible: false,
    })
  }

  render () {
    const {list} = this.props.users
    const {showModal, handleCancel, handleOk} = this
    const {loading} = this.state
    const AddModel = (
      <Modal title="添加新用户" className="admin-user__model" visible={this.state.visible} width="50%"
             onOk={handleOk} onCancel={handleCancel}
             footer={[
               <Button key="back" onClick={handleCancel}>取消</Button>,
               <Button key="submit" type="primary" loading={loading} onClick={handleOk}>
                 添加新用户
               </Button>,
             ]}>
        <p>Some contents...</p>
        <p>Some contents...</p>
        <p>Some contents...</p>
      </Modal>
    )
    return (
      <div className="admin-user">
        <div className="table-head">
          <h2>用户管理 <Icon type="user"/></h2>
          <Button onClick={showModal} type="dashed" className="table-add"><Icon type="plus-circle-o"/>新增用户</Button>
        </div>
        <Table columns={columns} dataSource={list} rowKey={'id'}/>
        {AddModel}
      </div>
    )
  }
}

export default UserView
