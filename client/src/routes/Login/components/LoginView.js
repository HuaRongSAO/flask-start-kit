import React from 'react'
import { Form, Icon, Input, Button, Checkbox } from 'antd'
import './LoginView.scss'
import LoginImg from '../assets/4.jpeg'

const FormItem = Form.Item
const rule = {
  username: {rules: [{required: true, message: '请输入邮箱'}]},
  password: {rules: [{required: true, message: '请输入密码'}]},
  remember: {valuePropName: 'checked', initialValue: true}
}

class LoginView extends React.Component {
  state = {}

  handleSubmit = async (e) => {
    e.preventDefault()
    this.props.loginAsync()
    this.props.form.validateFields((err, values) => {
      if (!err) {
        console.log('Received values of form: ', values)
      }
    })
  }

  render () {
    const {getFieldDecorator} = this.props.form
    return (
      <div className="login-box">
        <div className="login-form">
          <img src={LoginImg} className="login-img"/>
          <Form onSubmit={this.handleSubmit}>
            <FormItem
              label="Fail"
              hasFeedback
              validateStatus="error"
              help="Should be combination of numbers & alphabets">

              <Input hasFeedback prefix={<Icon type="user" style={{color: 'rgba(0,0,0,.25)'}}/>}
                     placeholder="Username@email.com"/>

            </FormItem>
            <FormItem>
              <Input hasFeedback prefix={<Icon type="lock" style={{color: 'rgba(0,0,0,.25)'}}/>} type="password"
                     placeholder="Password"/>
            </FormItem>
            <FormItem>
              <Checkbox>Remember me</Checkbox>
              <Button type="primary" htmlType="submit" className="login-form-button">
                登 入
              </Button>
              <p>
                <a className="login-form-forgot" href="">Forgot password</a>
                <a href="">register now!</a>
              </p>
            </FormItem>
          </Form>
        </div>
      </div>

    )
  }
}

export default Form.create()(LoginView)
