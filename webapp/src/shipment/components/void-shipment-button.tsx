import {
  Confirm,
  HttpError,
  useDataProvider,
  useNotify,
  useRecordContext,
  useRedirect,
  useResourceContext,
} from "react-admin";
import { useMutation, useQueryClient } from "react-query";
import { Button } from "@mui/material";
import { useState } from "react";
import WarningIcon from "@mui/icons-material/Warning";
import { ShipmentStatusType } from "../values/shipment-status-choices";

export function VoidShipmentButton() {
  const resource = useResourceContext();
  const notify = useNotify();
  const redirect = useRedirect();
  const queryClient = useQueryClient();

  const record = useRecordContext();
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const dataProvider = useDataProvider();
  const { mutate, isLoading } = useMutation(
    () => dataProvider.voidShipment(record.id),
    {
      retry: false,
      onError(error: HttpError) {
        notify(error.message, { type: "error" });
      },
    }
  );

  const handleClick = () => setIsDialogOpen(true);
  const handleCloseDialog = () => setIsDialogOpen(false);
  const handleConfirm = () => {
    mutate();
    queryClient.invalidateQueries({
      queryKey: [resource, "getList"],
    });
    setIsDialogOpen(false);
    redirect("list", "shipment");
  };

  if (!record) return null;
  if (
    record &&
    ![ShipmentStatusType.CONFIRMED, ShipmentStatusType.NOTIFIED].includes(
      record.status
    )
  )
    return null;
  return (
    <>
      <Button
        variant="contained"
        color="error"
        onClick={handleClick}
        disabled={isDialogOpen}
      >
        Void Shipment
      </Button>
      <Confirm
        title={`Void shipment #${record.id}`}
        content="Are you sure you want to void this shipment?"
        onClose={handleCloseDialog}
        onConfirm={handleConfirm}
        isOpen={isDialogOpen}
        loading={isLoading}
        confirmColor="warning"
        ConfirmIcon={WarningIcon}
        CancelIcon={() => null}
      />
    </>
  );
}
