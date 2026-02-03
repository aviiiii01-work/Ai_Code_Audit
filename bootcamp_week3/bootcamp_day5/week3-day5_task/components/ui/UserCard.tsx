import React from 'react';
import Card from './Card';

interface UserCardProps {
  name: string;
  email: string;
}

const UserCard: React.FC<UserCardProps> = ({ name, email }) => {
  return (
    <Card>
      <h3 className="text-lg font-semibold mb-1">{name}</h3>
      <p className="text-gray-600">{email}</p>
    </Card>
  );
};

export default UserCard;
