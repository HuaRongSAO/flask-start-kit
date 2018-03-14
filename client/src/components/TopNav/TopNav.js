import React from 'react'
import {Link, IndexLink} from 'react-router'
import {Menu, Icon, Button} from 'antd'
import './TopNav.scss'

const SubMenu = Menu.SubMenu
const MenuItemGroup = Menu.ItemGroup

class TopNav extends React.Component {
  state = {
    current: 'mail',
  }
  handleClick = (e) => {
    console.log('click ', e)
    this.setState({
      current: e.key,
    })
  }

  render() {
    return (
      <div className="container relative">
        <Menu
          onClick={this.handleClick}
          selectedKeys={[this.state.current]}
          mode="horizontal"
        >
          <Menu.Item key="logo">
            <IndexLink to="/"><Icon type="smile-o"/>Flask-react</IndexLink>
          </Menu.Item>
          <Menu.Item key="github">
            <a href="https://github.com/HuaRongSAO" target="_blank" rel="noopener noreferrer">
              <i className="icon icon-GitHub"></i>GitHub
            </a>
          </Menu.Item>
          <Menu.Item key="mail">
            <a href="https://www.jianshu.com/u/54f00e4dcf6e" target="_blank" rel="noopener noreferrer">
              <Icon type="database"/>blog
            </a>
          </Menu.Item>
        </Menu>
        <Button className="login-btn" type="danger" size="large"><Link to="/login"><Icon type="user-add"/> login</Link></Button>
      </div>
    )
  }
}

export default TopNav
