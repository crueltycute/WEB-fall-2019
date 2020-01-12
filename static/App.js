import React from 'react';
import ReactDOM from 'react-dom';
import List from './components/List/List.js';

import './css/style.css';

const USERNAME = 'crueltycute';

const element = <List username={USERNAME} />;
ReactDOM.render(element, document.getElementById('root'));