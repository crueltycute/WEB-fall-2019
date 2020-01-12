import React from 'react';

import './ListItem.css';

export default class ListItem extends React.Component {
    render() {
        return (
            <li>{ this.props.value }</li>
        );
    }
}