import React from 'react';
import axios from 'axios';

import './List.css';

import ListItem from '../ListItem/ListItem.js';

export default class List extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            username: this.props.username,
            reposList: []
        }
    }

    componentWillMount() {
        this.initReposList();
    }

    initReposList() {
        axios.get('https://api.github.com/users/' + this.state.username + '/repos')
            .then(res => {
                this.state.reposList = res.data.map(repo => {
                    return <ListItem key={ repo.id } value={ repo.name }/>;
                });
                this.setState(this.state.reposList);
            });
    }

    render() {
        return (
            <div className={'repo-list'}>
                <h1 className={'repo-list__header'}>{ this.props.username }'s repos:</h1>
                <ul className={'repo-list__content'}>
                    { this.state.reposList }
                </ul>
            </div>
        );
    }
}