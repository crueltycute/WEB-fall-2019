import React from 'react';
import axios from 'axios';

import ListItem from './List';

export default class List extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            username: this.props.username,
            reposList: []
        }
    }

    componentDidMount() {
        this.initReposList();
    }

    initReposList() {
        axios.get('https://api.github.com/users/' + this.state.username + '/repos')
            .then(res => {
                this.state.reposList = res.data.map(repo => {
                    return { id: repo.id, value: repo.name }
                });
            });
    }

    render() {
        return (
            <div>
                <h1>{ this.props.username }'s repos:</h1>
                <ul>
                    { this.state.reposList.map(repo => {
                            <ListItem value={repo}/>
                        })
                    }
                </ul>
            </div>
        );
    }
}