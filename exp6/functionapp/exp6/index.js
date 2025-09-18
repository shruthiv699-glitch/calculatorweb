module.exports = async function (context, req) {
  context.log('HTTP trigger processed a request.');
  context.res = {
    status: 200,
    body: "Hello Elasticity!"
  };
};
