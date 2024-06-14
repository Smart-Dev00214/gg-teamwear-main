import {
  Datagrid,
  DateField,
  ReferenceManyField,
  ReferenceOneField,
  SelectField,
  Show,
  SimpleShowLayout,
  TextField,
} from "react-admin";
import { FileFromRecordField } from "../../common/components/file-from-record-field";
import { ShipmentStatusChoices } from "../values/shipment-status-choices";
import { CourierChoices } from "../values/courier-choices";
import { ShipmentShowDatagridBulkActionButtons } from "../components/shipment-show-datagrid-bulk-action-buttons";
import { VoidShipmentButton } from "../components/void-shipment-button";
import { SendASNButton } from "../components/send-asn-button";

export const ShipmentShow = () => (
  <Show>
    <SimpleShowLayout>
      <TextField source="id" />
      <SelectField source="status" choices={ShipmentStatusChoices} />
      <SelectField source="courier" choices={CourierChoices} />
      <TextField source="shipmentIdentificationNumber" />
      <DateField source="date" showTime />
      <DateField source="estimatedDeliveryDate" />
      <TextField source="charge" />
      <TextField source="chargeWithTax" />
      <TextField source="billingWeight" />
      <TextField source="disclaimer" />
      <ReferenceOneField
        label="Customs document"
        reference="customs-document"
        target="shipmentId"
        emptyText="None"
      >
        <TextField source="name" />
      </ReferenceOneField>
      <SendASNButton />
      <TextField source="error" emptyText="None" />
      <ReferenceManyField
        reference="shipment-package"
        target="shipmentId"
        label="Packages"
        perPage={1000}
      >
        <Datagrid bulkActionButtons={<ShipmentShowDatagridBulkActionButtons />}>
          <TextField source="trackingNumber" label="Tracking number" />
          <FileFromRecordField
            source="label"
            filename={(record) => `package-label-${record.trackingNumber}.zpl`}
          />
        </Datagrid>
      </ReferenceManyField>
      <VoidShipmentButton />
    </SimpleShowLayout>
  </Show>
);
