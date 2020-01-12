import React from 'react';
import ReactDOM from 'react-dom';
import List from './components/List/';

const USERNAME = 'crueltycute';

const element = <List username={USERNAME} />;
ReactDOM.render(element, document.getElementById('root'));