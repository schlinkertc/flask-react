import React from 'react';
import { List, Header } from "semantic-ui-react";


export const Pitches = ({ pitches }) => {
  return (
    <List>
     {pitches.map(pitch => {
       return (
         <List.Item key={pitch.pitchType}>
          <Header>{pitch.pitchType}: {pitch.avg_startSpeed}</Header>
         </List.Item>
       )
     })}
    </List>
  )
};
