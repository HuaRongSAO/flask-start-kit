// rcd +回车
import React from 'react'
import PropTypes from 'prop-types'
import { Modal, Button, Form, Input, Icon } from 'antd'

const FormItem = Form.Item

class UserModal extends React.Component {
  state = {
    user: {
      username: {value: '', status: '', msg: ''},
      phone: {value: '', status: '', msg: ''},
      email: {value: '', status: '', msg: ''},
      password: {value: '', status: '', msg: ''},
    }
  }
  // 渲染icon
  renderIcon = type => (<Icon type={type} style={{color: 'rgba(0,0,0,.25)'}}/>)
  // 提交
  handleSubmit = () => {

  }
  // 验证规则
  userRule = (target, value) => {
    const formItem = {}
    formItem.value = value
    let reg = {
      username: /^[\u0391-\uFFE5]+$/,
      phone: /^1[3|4|5|8][0-9]\d{8}$ /,
      email: /^[a-zA-Z_]{1,}[0-9]{0,}@(([a-zA-z0-9]-*){1,}\.){1,3}[a-zA-z\-]{1,}$ /,
      password: /^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,21}$/
    }
    if (reg[target].test(value)) {
      return {value, status: 'success', msg: ''}
    }
    return {value, status: 'error', msg: ''}
  }
  // 修改
  onChange = (e, target) => {
    const user = this.state.user
    user[target] = this.userRule(target, e.target.value)
    this.setState(user)
  }

  render () {
    const {handleSubmit, onChange, renderIcon} = this
    const {handleCancel, handleOk, loading, visible} = this.props
    const {email, username, phone, password} = this.state.user
    const footer = [<Button key="back" onClick={handleCancel}>取消</Button>,
      <Button key="submit" type="primary" loading={loading} onClick={handleOk}>添加新用户</Button>]
    const formItemLayout = {
      labelCol: {xs: {span: 24}, sm: {span: 4},},
      wrapperCol: {xs: {span: 24}, sm: {span: 20},},
    }
    return (
      <Modal title="添加新用户" className="admin-user__model" visible={visible} width="50%"
             onOk={handleOk} onCancel={handleCancel}
             footer={footer}>
        <div className="form-box flex-center">
          <Form onSubmit={handleSubmit} className="user-modal__form">
            <FormItem  {...formItemLayout} label="账号" hasFeedback
                       validateStatus={username.status} help={username.message}>
              <Input prefix={renderIcon('user')} onChange={e => {onChange(e, 'username')}}
                     placeholder="用户名" value={username.value}/>
            </FormItem>
            <FormItem  {...formItemLayout} label="邮箱" hasFeedback
                       validateStatus={email.status} help={email.message}>
              <Input prefix={renderIcon('paper-clip')} onChange={e => {onChange(e, 'email')}}
                     placeholder="邮箱" value={email.value}/>
            </FormItem>
            <FormItem  {...formItemLayout} label="手机" hasFeedback
                       validateStatus={phone.status} help={phone.message}>
              <Input prefix={renderIcon('phone')} onChange={e => {onChange(e, 'phone')}}
                     placeholder="手机" value={phone.value}/>
            </FormItem>
            <FormItem  {...formItemLayout} label="密码" hasFeedback
                       validateStatus={password.status} help={password.message}>
              <Input type="password" prefix={renderIcon('lock')} onChange={e => {onChange(e, 'password')}}
                     placeholder="密码" value={password.value}/>
            </FormItem>
          </Form>
        </div>

      </Modal>
    )
  }
}

UserModal.propTypes = {
  handleCancel: PropTypes.func.isRequired,
  handleOk: PropTypes.func.isRequired,
  loading: PropTypes.bool.isRequired,
  visible: PropTypes.bool.isRequired
}
export default Form.create()(UserModal)
