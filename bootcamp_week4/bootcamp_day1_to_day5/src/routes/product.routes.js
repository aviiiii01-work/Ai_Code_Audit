const router = require("express").Router();
const controller = require("../controllers/product.controller");

const validate = require("../middlewares/validate");
const ProductSchema = require("../validators/product.schema");

router.post("/", validate(ProductSchema), controller.createProduct);
router.get("/:id", controller.getProduct);
router.get("/", controller.getProductsPaginated);
router.delete("/:id", controller.deleteProduct);

module.exports = router;
