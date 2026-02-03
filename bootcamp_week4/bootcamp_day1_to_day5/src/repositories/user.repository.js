const User = require("../models/User");

class UserRepository {
  async create(data) {
    return User.create(data);
  }

  async findById(id) {
    return User.findById(id);
  }

  async findPaginated(page = 1, limit = 10) {
    const skip = (page - 1) * limit;
    return User.find().skip(skip).limit(limit).sort({ createdAt: -1 });
  }

  async update(id, data) {
    return User.findByIdAndUpdate(id, data, { new: true });
  }

  async delete(id) {
    return User.findByIdAndDelete(id);
  }
}

module.exports = new UserRepository();
