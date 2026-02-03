const router = require("express").Router();
const controller = require("../controllers/user.controller");

const validate = require("../middlewares/validate");
const UserSchema = require("../validators/user.schema");

router.post("/", validate(UserSchema), controller.createUser);
router.get("/:id", controller.getUser);
router.get("/", controller.getUsersPaginated);
router.post("/send-email", controller.sendWelcomeEmail);

module.exports = router;
