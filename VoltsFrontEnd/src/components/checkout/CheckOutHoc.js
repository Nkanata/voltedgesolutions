import React, {Component} from "react";
import {connect} from 'react-redux'
import Checkout from "./Checkout";


class CheckOutHoc extends Component {
    constructor(props) {
        super(props);

        this.state = {
            firstName: '',
            lastName: '',
            email: '',
            address1: '',
            postal_code: '',
            phone: '',
            county: '',
            city: '',
            Country: 'Kenya',
            order_items: [],
            res: {},
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleRes = this.handleRes.bind(this);
    };

    componentDidMount() {
        this.setState({
            ...this.state,
            order_items: this.props.orderItems,
            res: []
        })
    }

    handleChange = (e) => {
        this.setState({
            [e.target.id]: e.target.value
        })
    };
    handleRes = (res) => {
        this.setState({
            ...this.state,
            res
        })
    };

    render() {
        return (
            <Checkout handleChange={this.handleChange} state={this.state} handleRes={this.handleRes}/>
        )

    }

}

const mapStateToProps = (state) => {
    return {
        orderItems: state.orders.order,
        res: state.orders.res
    }
};

export default connect(mapStateToProps)(CheckOutHoc)