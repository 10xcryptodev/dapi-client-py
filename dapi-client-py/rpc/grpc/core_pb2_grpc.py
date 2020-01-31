# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import core_pb2 as core__pb2


class CoreStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getStatus = channel.unary_unary(
        '/org.dash.platform.dapi.v0.Core/getStatus',
        request_serializer=core__pb2.GetStatusRequest.SerializeToString,
        response_deserializer=core__pb2.GetStatusResponse.FromString,
        )
    self.getBlock = channel.unary_unary(
        '/org.dash.platform.dapi.v0.Core/getBlock',
        request_serializer=core__pb2.GetBlockRequest.SerializeToString,
        response_deserializer=core__pb2.GetBlockResponse.FromString,
        )
    self.sendTransaction = channel.unary_unary(
        '/org.dash.platform.dapi.v0.Core/sendTransaction',
        request_serializer=core__pb2.SendTransactionRequest.SerializeToString,
        response_deserializer=core__pb2.SendTransactionResponse.FromString,
        )
    self.getTransaction = channel.unary_unary(
        '/org.dash.platform.dapi.v0.Core/getTransaction',
        request_serializer=core__pb2.GetTransactionRequest.SerializeToString,
        response_deserializer=core__pb2.GetTransactionResponse.FromString,
        )
    self.getEstimatedTransactionFee = channel.unary_unary(
        '/org.dash.platform.dapi.v0.Core/getEstimatedTransactionFee',
        request_serializer=core__pb2.GetEstimatedTransactionFeeRequest.SerializeToString,
        response_deserializer=core__pb2.GetEstimatedTransactionFeeResponse.FromString,
        )
    self.subscribeToBlockHeadersWithChainLocks = channel.unary_stream(
        '/org.dash.platform.dapi.v0.Core/subscribeToBlockHeadersWithChainLocks',
        request_serializer=core__pb2.BlockHeadersWithChainLocksRequest.SerializeToString,
        response_deserializer=core__pb2.BlockHeadersWithChainLocksResponse.FromString,
        )


class CoreServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def getStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getBlock(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def sendTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getTransaction(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getEstimatedTransactionFee(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def subscribeToBlockHeadersWithChainLocks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CoreServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getStatus': grpc.unary_unary_rpc_method_handler(
          servicer.getStatus,
          request_deserializer=core__pb2.GetStatusRequest.FromString,
          response_serializer=core__pb2.GetStatusResponse.SerializeToString,
      ),
      'getBlock': grpc.unary_unary_rpc_method_handler(
          servicer.getBlock,
          request_deserializer=core__pb2.GetBlockRequest.FromString,
          response_serializer=core__pb2.GetBlockResponse.SerializeToString,
      ),
      'sendTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.sendTransaction,
          request_deserializer=core__pb2.SendTransactionRequest.FromString,
          response_serializer=core__pb2.SendTransactionResponse.SerializeToString,
      ),
      'getTransaction': grpc.unary_unary_rpc_method_handler(
          servicer.getTransaction,
          request_deserializer=core__pb2.GetTransactionRequest.FromString,
          response_serializer=core__pb2.GetTransactionResponse.SerializeToString,
      ),
      'getEstimatedTransactionFee': grpc.unary_unary_rpc_method_handler(
          servicer.getEstimatedTransactionFee,
          request_deserializer=core__pb2.GetEstimatedTransactionFeeRequest.FromString,
          response_serializer=core__pb2.GetEstimatedTransactionFeeResponse.SerializeToString,
      ),
      'subscribeToBlockHeadersWithChainLocks': grpc.unary_stream_rpc_method_handler(
          servicer.subscribeToBlockHeadersWithChainLocks,
          request_deserializer=core__pb2.BlockHeadersWithChainLocksRequest.FromString,
          response_serializer=core__pb2.BlockHeadersWithChainLocksResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'org.dash.platform.dapi.v0.Core', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))