import React, { Component } from 'react'

export default class Demon extends Component {


  componentDidMount = () => {
    console.log(this.props);
  }


  catchDemons = async () => {
    const url = `http://127.0.0.1:5000/catch_demon/${this.props.demonInfo.name}`

    const options = {
      method: "POST",
      headers: { Authorization: `Bearer ${this.props.user.apitoken}` }
    }

    const res = await fetch(url, options);
    const data = await res.json();
    console.log(data)
    if (data.status === 'ok') {
      // this.setState({}) catch successful, redirect to profile page
    }


  }




  render() {
    return (

      <div className="card" style={{ margin: "auto", padding: "1px", width: "24rem", color: "#bb83f2", fontSize: "34px", textAlign: "center" }}>
        <div className="card-body">
          <img src={`http://smt-app1111.b-cdn.net/${this.props.demonInfo.name}.png`} style={{ width: "22rem", imageRendering:"auto" }} />
          <h5 className="card-title" style={{ fontSize: "80px", color: "#bb83f2", letterSpacing: "5px", lineHeight: "1.5", textShadow: "-1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000" }}>{this.props.demonInfo.name}</h5>
          <p className="card-text" style={{ lineHeight: "0.8" }}>Hp: {this.props.demonInfo.hp}</p>
          {/* <p className="card-text">Alignment:{this.props.demonInfo.alignment.ethical}-{this.props.demonInfo.alignment.moral}</p> */}
          <p className="card-text" style={{ lineHeight: "0.8" }}>Strength: {this.props.demonInfo.strength}</p>
          <p className="card-text" style={{ lineHeight: "0.8" }}>Magic: {this.props.demonInfo.magic}</p>
          <p className="card-text" style={{ lineHeight: "0.8" }}>Defense: {this.props.demonInfo.defense}</p>
          <button onClick={this.catchDemons} className="btn btn-primary">Catch</button>
        </div>
      </div>
    )
  }
}
